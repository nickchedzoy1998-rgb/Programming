-- Sample input data for SQL exercise 03. Do not edit.
CREATE TABLE market_observations (
    observation_id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    observed_at TEXT NOT NULL,
    price REAL NOT NULL,
    status TEXT NOT NULL
);

INSERT INTO market_observations
(observation_id, symbol, observed_at, price, status) VALUES
    (1, 'ABC', '2026-11-01T09:00:00', 100.00, 'valid'),
    (2, 'ABC', '2026-11-01T09:05:00', 101.00, 'valid'),
    (3, 'ABC', '2026-11-01T09:10:00', 999.00, 'rejected'),
    (4, 'XYZ', '2026-11-01T09:01:00', 54.00, 'valid'),
    (5, 'XYZ', '2026-11-01T09:05:00', 55.00, 'valid'),
    (6, 'XYZ', '2026-11-01T09:05:00', 56.00, 'valid'),
    (7, 'QRS', '2026-11-01T09:05:00', 100.00, 'rejected'),
    (8, 'QRS', '2026-11-01T09:03:00', 80.00, 'valid'),
    (9, 'NEW', '2026-11-01T09:00:00', 120.00, 'rejected'),
    (10, 'MM', '2026-11-01T09:00:00', 70.00, 'valid');
