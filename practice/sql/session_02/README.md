# SQL Session 02 — Latest transaction per customer

This exercise introduces window functions using a small transaction dataset.

## Your task

Write **one SQL query** that returns the **most recent transaction for each customer**, including:

- `transaction_id`
- `customer_id`
- `transaction_date`
- `amount_gbp`

Expected output:

| transaction_id | customer_id | transaction_date | amount_gbp |
| --- | --- | --- | ---: |
| 103 | A | 2026-01-10 | 30 |
| 105 | B | 2026-01-08 | 60 |

## Files

- **`work.sql` — edit this file** to write your SQL query.
- `setup.sql` — creates the sample table and loads the data (leave unchanged).
- `run.py` — runs your SQL against a fresh in-memory SQLite database and prints the result.

## Run

From the root of your local Programming repository:

```powershell
git pull
python practice/sql/session_02/run.py
```

No database server or additional packages are required. The runner intentionally does not include an answer.
