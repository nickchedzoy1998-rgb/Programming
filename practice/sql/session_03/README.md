# SQL exercise 03 — Latest valid market observation

**Write your own solution in `work.sql`.** This exercise reviews concepts from the previous SQL exercises without providing a solution.

## Scenario

A market-data system records observations for multiple instruments. Each observation contains:

- `observation_id` — a unique integer ID
- `symbol` — instrument identifier
- `observed_at` — timestamp (ISO 8601 text)
- `price` — price as a decimal
- `status` — either `valid` or `rejected`

The `market_observations` table is populated automatically.

## Task

Return **the latest valid observation for each symbol**.

Requirements:

1. Include only observations where `status = 'valid'`.
2. Return **exactly one row per symbol**.
3. If multiple valid observations share the latest timestamp for a symbol, select the one with the **highest `observation_id`**.
4. A symbol with no valid observations should not appear.
5. Order results by `symbol` ascending.

Return these four columns, in order:

`symbol`, `observation_id`, `observed_at`, `price`.

There should be **four result rows** for the provided dataset.

## Workflow

1. Edit **`work.sql`**. Don't change the sample data or runner.
2. Run the command below from the **Programming repository root**.
3. Share your SQL query and/or output for feedback.

```powershell
python practice/sql/session_03/run.py
```

No database installation or third-party dependencies required. The database is recreated in memory each time. The files contain no solution or code hints.
