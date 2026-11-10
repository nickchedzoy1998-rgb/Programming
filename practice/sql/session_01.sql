-- SQL practice: Session 01, exercise 01
-- Dialect: SQLite (standard SQL features are sufficient).
--
-- Your objective: write a correct query independently and explain it.
-- Run the setup statements once in a new, empty SQLite database.

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    customer_id TEXT NOT NULL,
    amount_gbp INTEGER NOT NULL
);

CREATE TABLE refunds (
    refund_id INTEGER PRIMARY KEY,
    transaction_id INTEGER NOT NULL REFERENCES transactions(transaction_id),
    amount_gbp INTEGER NOT NULL
);

INSERT INTO transactions (transaction_id, customer_id, amount_gbp) VALUES
    (101, 'A', 120),
    (102, 'A', 75),
    (103, 'B', 200),
    (104, 'B', 45),
    (105, 'C', 60);

INSERT INTO refunds (refund_id, transaction_id, amount_gbp) VALUES
    (1, 101, 20),
    (2, 101, 35),
    (3, 103, 50),
    (4, 104, 45);

-- EXERCISE 01 (attempt without looking up a solution)
--
-- Return exactly one row per customer with:
--   customer_id
--   net_revenue_gbp: sum of their transaction amounts minus their refunds
--
-- Requirements:
-- - Some transactions have no refunds.
-- - A transaction may have multiple partial refunds.
-- - Avoid accidentally counting a transaction more than once.
-- - Sort by customer_id ascending.
--
-- Expected result:
-- customer_id | net_revenue_gbp
-- ------------+----------------
-- A           | 140
-- B           | 150
-- C           | 60
--
-- Write your query below. Explain your approach aloud first.
--
