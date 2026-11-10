-- SQL exercise 03.
-- Write your SELECT query below.
-- The table market_observations is created by run.py.

with ordered_observations AS (
    SELECT
        observation_id,
        symbol,
        observed_at,
        price,
        status,
        ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY observed_at DESC, observation_id DESC) AS time_order
    FROM market_observations
    WHERE status = 'valid'
)
SELECT *
FROM ordered_observations
WHERE time_order = 1
ORDER BY symbol ASC
;
    


-- python practice/sql/session_03/run.py