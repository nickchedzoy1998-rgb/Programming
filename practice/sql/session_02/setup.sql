-- Example data for SQL Session 02. Leave unchanged.
CREATE TABLE dated_transactions (
    transaction_id INTEGER PRIMARY KEY,
    customer_id TEXT NOT NULL,
    transaction_date TEXT NOT NULL,
    amount_gbp INTEGER NOT NULL
);

INSERT INTO dated_transactions (
    transaction_id, customer_id, transaction_date, amount_gbp
) VALUES
    (101, 'A', '2026-01-01', 50),
    (102, 'A', '2026-01-05', 100),
    (103, 'A', '2026-01-10', 30),
    (104, 'B', '2026-01-03', 80),
    (105, 'B', '2026-01-08', 60);
