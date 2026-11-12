"""Process and validate a batch of transaction records.

See README.md for the input contract and output format.
"""


def process_transactions(records: list[dict[str, str]]) -> tuple[list[dict], list[dict]]:
    """Return (accepted, rejected) records without modifying input."""

    output_records = []
    rejected_records = []

    valid_currencies = ['GBP', 'USD']

    def valid_amount(amount: str) -> bool:        
        # Check is a number
        try:
            float(amount)
        except ValueError:
            return False

        # Greater than 0
        if float(amount) <= 0:
            return False

        if '.' in amount:
            dec_places = amount.split('.')
            if len(dec_places[1]) > 2:
                return False

        return True

    for i, record in enumerate(records):
        id = record.get('transaction_id', '')
        id = id.strip()

        if id == '':
            rejected_records.append({'index': i, 'reason': 'missing_id'})
            continue

        amount = record.get('amount', '')

        if valid_amount(amount) == False:
            rejected_records.append({'index': i, 'reason': 'invalid_amount'})
            continue

        amount_cents = int(float(amount)) * 100

        currency = record.get('currency', 'none').strip().upper()

        if currency not in valid_currencies:
            rejected_records.append({'index': i, 'reason': 'unsupported_currency'})
            continue

        if id in [rec['transaction_id'] for rec in output_records]:
            rejected_records.append({'index': i, 'reason': 'duplicate_id'})
            continue

        output_records.append(
            {"transaction_id": id, "amount_cents": amount_cents, "currency": currency}
        )

    return (output_records, rejected_records)






"""
### Input

Each record is expected to have:

- `transaction_id` — a non-empty string identifying the transaction
- `amount` — an amount in pounds/dollars expressed as a string, for example `"12.50"`
- `currency` — a string such as `"gbp"` or `"USD"`

Any of these fields may be absent. Treat leading/trailing whitespace as insignificant.

### Required behaviour

For each record, in input order:

1. **ID:** Remove surrounding whitespace. Reject a missing or empty ID with reason `"missing_id"`.
2. **Amount:** Accept only **strictly positive** amounts with no more than **two decimal places**. `"12"`, `"12.5"` and `"12.50"` are valid; `"0"`, `"-3"`, `"abc"`, `"12.345"` and `"NaN"` are invalid. Reject invalid or missing amounts with reason `"invalid_amount"`. Do not silently round.
3. **Currency:** Strip whitespace and convert to uppercase. Only `GBP` and `USD` are supported. Reject missing/unsupported currencies with reason `"unsupported_currency"`.
4. **Duplicates:** If a transaction ID has **already been accepted** earlier in the same batch, reject the later record with reason `"duplicate_id"`. An earlier *rejected* record does **not** reserve its ID.

If a record has several problems, apply the validation rules **in the order above**, reporting the first applicable rejection reason.

### Output

Return a two-item tuple: `(accepted, rejected)`.

- `accepted`: list of dictionaries with **exactly** these keys:
  - `"transaction_id"`: trimmed ID (string)
  - `"amount_cents"`: amount in the smallest currency unit (integer; e.g., `"12.50"` → `1250`)
  - `"currency"`: `"GBP"` or `"USD"`
- `rejected`: list of dictionaries with **exactly** these keys:
  - `"index"`: original **0-based input position** (integer)
  - `"reason"`: one of the four reason strings above

Preserve input order within each output list. Do not modify the input records.

### Example

Input:

```python
records = [
    {"transaction_id": " T1 ", "amount": "12.50", "currency": "gbp"},
    {"transaction_id": "T2", "amount": "not-a-number", "currency": "GBP"},
    {"transaction_id": "T1", "amount": "4", "currency": "GBP"},
    {"transaction_id": "T3", "amount": "1.2", "currency": "usd"},
]
```

Expected output:

```python
(
    [
        {"transaction_id": "T1", "amount_cents": 1250, "currency": "GBP"},
        {"transaction_id": "T3", "amount_cents": 120, "currency": "USD"},
    ],
    [
        {"index": 1, "reason": "invalid_amount"},
        {"index": 2, "reason": "duplicate_id"},
    ],
)"""
