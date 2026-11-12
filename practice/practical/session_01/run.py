"""Run the transaction processing checks (Python standard library only).

From the Programming repository root:
    python practice/practical/session_01/run.py
"""
import unittest

from solution import process_transactions


class TransactionProcessingTests(unittest.TestCase):
    def test_mixed_batch(self):
        records = [
            {"transaction_id": " T1 ", "amount": "12.50", "currency": "gbp"},
            {"transaction_id": "T2", "amount": "not-a-number", "currency": "GBP"},
            {"transaction_id": "T1", "amount": "4", "currency": "GBP"},
            {"transaction_id": "T3", "amount": "1.2", "currency": "usd"},
        ]
        snapshot = [record.copy() for record in records]
        accepted, rejected = process_transactions(records)
        self.assertEqual(accepted, [
            {"transaction_id": "T1", "amount_cents": 1250, "currency": "GBP"},
            {"transaction_id": "T3", "amount_cents": 120, "currency": "USD"},
        ])
        self.assertEqual(rejected, [
            {"index": 1, "reason": "invalid_amount"},
            {"index": 2, "reason": "duplicate_id"},
        ])
        self.assertEqual(records, snapshot, "Input dictionaries must not be modified.")

    def test_empty_batch(self):
        self.assertEqual(process_transactions([]), ([], []))

    def test_missing_fields_and_validation_priority(self):
        records = [
            {"amount": "5.00", "currency": "GBP"},
            {"transaction_id": " ", "amount": "x", "currency": "EUR"},
            {"transaction_id": "A", "currency": "GBP"},
            {"transaction_id": "B", "amount": "3.00"},
            {"transaction_id": "C", "amount": "2.50", "currency": "EUR"},
        ]
        self.assertEqual(process_transactions(records), ([], [
            {"index": 0, "reason": "missing_id"},
            {"index": 1, "reason": "missing_id"},
            {"index": 2, "reason": "invalid_amount"},
            {"index": 3, "reason": "unsupported_currency"},
            {"index": 4, "reason": "unsupported_currency"},
        ]))

    def test_invalid_amounts_not_rounded(self):
        amounts = ["0", "-3.00", "12.345", "abc", "NaN", "Infinity", "", "  "]
        records = [
            {"transaction_id": f"T{i}", "amount": amount, "currency": "GBP"}
            for i, amount in enumerate(amounts)
        ]
        accepted, rejected = process_transactions(records)
        self.assertEqual(accepted, [])
        self.assertEqual(rejected, [
            {"index": index, "reason": "invalid_amount"}
            for index in range(len(amounts))
        ])

    def test_first_rejected_does_not_claim_id(self):
        records = [
            {"transaction_id": "A", "amount": "bad", "currency": "GBP"},
            {"transaction_id": " A ", "amount": "0.01", "currency": " gbp "},
            {"transaction_id": "A", "amount": "9.99", "currency": "GBP"},
        ]
        self.assertEqual(process_transactions(records), (
            [{"transaction_id": "A", "amount_cents": 1, "currency": "GBP"}],
            [
                {"index": 0, "reason": "invalid_amount"},
                {"index": 2, "reason": "duplicate_id"},
            ],
        ))

    def test_decimal_precision_and_input_order(self):
        records = [
            {"transaction_id": "A", "amount": "0.10", "currency": "GBP"},
            {"transaction_id": "B", "amount": "0.20", "currency": "USD"},
            {"transaction_id": "C", "amount": "120", "currency": "GBP"},
            {"transaction_id": "D", "amount": "1.5", "currency": "USD"},
        ]
        accepted, rejected = process_transactions(records)
        self.assertEqual(accepted, [
            {"transaction_id": "A", "amount_cents": 10, "currency": "GBP"},
            {"transaction_id": "B", "amount_cents": 20, "currency": "USD"},
            {"transaction_id": "C", "amount_cents": 12000, "currency": "GBP"},
            {"transaction_id": "D", "amount_cents": 150, "currency": "USD"},
        ])
        self.assertEqual(rejected, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
