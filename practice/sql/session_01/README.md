# SQL Session 01 — Transactions and refunds

**Edit only `work.sql`.** The other files are provided so you can run your query without setting up a database.

## The task

For each customer, calculate net revenue = total transaction amount minus total refunds.
Some transactions have multiple refunds; others have none. Each transaction amount must be counted only once.

Expected final result:

| customer_id | net_revenue_gbp |
| --- | ---: |
| A | 140 |
| B | 150 |
| C | 60 |

## Approach — one step at a time

1. **Current:** Query `refunds` to obtain one row per `transaction_id`, showing the total refund amount for that transaction.
2. **Next:** Join those totals to `transactions`. Keep transactions with no refund, and avoid multiplying transaction rows.
3. **Finally:** Calculate one net total per customer.

No need to create tables manually. They are created in a fresh temporary in-memory SQLite database every run, using `setup.sql`.

## How to run it

From the root of your local Programming repository:

```bash
python practice/sql/session_01/run.py
```

Write your SQL in `work.sql`, run the command, then send your SQL or the output for feedback. **The runner executes your query; it does not reveal the solution.**

## Files

- `work.sql` — your only editable SQL file for this session.
- `setup.sql` — creates and populates the `transactions` and `refunds` tables.
- `run.py` — creates a clean SQLite database and executes `work.sql`.

SQL dialect: SQLite, with ordinary standard SQL constructs.
