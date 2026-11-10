-- YOUR WORKSPACE. Write exactly one SQL SELECT query below.
--
-- CURRENT STEP: Calculate total refunded per transaction.
-- Use the refunds table, SUM(amount_gbp), and GROUP BY transaction_id.
--
-- When that works, we'll extend the query to include transactions with no refunds
-- and finally calculate net revenue per customer.
-- You can replace/edit the query below as we progress.

WITH refund_totals AS (
    SELECT
        transaction_id,
        SUM(amount_gbp) AS total_refund
    FROM refunds
    GROUP BY transaction_id
)
SELECT
    tr.customer_id,
    SUM(tr.amount_gbp) - SUM(IFNULL(rt.total_refund, 0)) AS net_revenue_gbp
FROM transactions AS tr
LEFT JOIN refund_totals AS rt ON tr.transaction_id = rt.transaction_id
GROUP BY tr.customer_id
;

SELECT 
    customer_id,
    SUM(amount_gbp) AS total_spent
FROM transactions
WHERE amount_gbp >= 50
GROUP BY customer_id
HAVING total_spent > 100
ORDER BY total_spent DESC
;

-- python practice/sql/session_01/run.py