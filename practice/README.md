# Technical Interview Practice

A compact workspace for practising independent problem-solving in Python, SQL, and data engineering.

## Four-session plan

| Session | Focus | Status |
| --- | --- | --- |
| 1 | SQL: joins, aggregation, CTEs, window functions and correctness checks | In progress |
| 2 | Python algorithms: timed unfamiliar problems, complexity and edge cases | Not started |
| 3 | Practical engineering: validation, transformations, testing and rerun safety | Not started |
| 4 | Mock technical interview: an unseen task, follow-up requirements and review | Not started |

## Start here

**SQL exercises:** [Session 01 — transactions and refunds](sql/session_01/README.md) · [Session 02 — latest transaction per customer](sql/session_02/README.md) · [Session 03 — latest valid market observation](sql/session_03/README.md)

- Edit `sql/session_01/work.sql` to write your query.
- `sql/session_01/setup.sql` contains the example tables and data (do not edit).
- Run: `python practice/sql/session_01/run.py` from the repository root.

Only `work.sql` needs to be edited for this exercise. A new SQLite database is created in memory on each run.

## Working approach

1. Attempt unfamiliar exercises independently before receiving hints.
2. Clarify inputs, expected output and edge cases before coding.
3. Prefer plain `.py` and `.sql` files, with tests where useful.
4. Explain the approach, trade-offs and failure modes.
5. Review mistakes and revisit weak concepts with a fresh exercise.

Future exercises will be added as needed. Content and commits remain company-neutral.
