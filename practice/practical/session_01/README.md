# Practical Python — Session 01: Transaction batch cleaner

## Scenario

A data pipeline receives transaction records from an external source. The input is a list of dictionaries; fields may be malformed or missing. Build a **pure Python function** that separates accepted records from rejected records.

Implement this function in **`solution.py`**:

```python
def process_transactions(records: list[dict[str, str]]) -> tuple[list[dict], list[dict]]:
    ...
```

### Input

Each record is expected to have:

- `transaction_id` — a non-empty string identifying the transaction
- `amount` — an amount in pounds/dollars expressed as a string, for example `"12.50"`
- `currency` — a string such as `"gbp"` or `"USD"`

Any of these fields may be absent. Treat leading/trailing whitespace as insignificant.

### Required behaviour

For each record, in input order:

1. **ID:** Remove surrounding whitespace. Reject a missing or empty ID with reason `"missing_id"`.
2. **Amount:** Accept only **strictly positive** amounts with no more than **two decimal places**. `"12"`, `"12.5"` and `"12.50"` are valid; `"0"`, `"-3"`, `"abc"`, `"12.345"` is invalid. Reject invalid or missing amounts with reason `"invalid_amount"`. Do not silently round.
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
)
```

## Workflow

1. Edit **`solution.py`** (only this file is needed).
2. From the Programming repository root, run:

```powershell
python practice/practical/session_01/run.py
```

3. Share your first attempt for review.

**Suggested time:** 30–40 minutes, followed by a short discussion of design choices, testing, edge cases and scaling.

No third-party packages are required. The test runner contains no solution or implementation hints.

**Practice scope:** This exercise covers ordinary decimal-string amounts with at most two decimal places. Special floating-point representations such as `NaN` and `Infinity` and very large amounts are intentionally not tested. In real financial systems, exact decimal arithmetic and additional input validation are recommended.
