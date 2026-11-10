-- SQL Session 02: Write your query below.
-- The table dated_transactions is created automatically by run.py.
-- Goal: return the latest transaction for each customer.
-- Do not edit setup.sql.
WITH date_ranks AS (
    SELECT
        transaction_id,
        customer_id,
        transaction_date,
        amount_gbp,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_date DESC) as date_rank
    FROM dated_transactions
)
SELECT
    transaction_id,
    customer_id,
    transaction_date,
    amount_gbp
FROM date_ranks
WHERE date_rank = 1
;

-- python practice/sql/session_02/run.py