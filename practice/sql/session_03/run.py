"""Execute the query in work.sql against an in-memory SQLite database.

From the Programming repository root:
    python practice/sql/session_03/run.py
"""
from pathlib import Path
import sqlite3

folder = Path(__file__).resolve().parent
setup = (folder / "setup.sql").read_text(encoding="utf-8")
query = (folder / "work.sql").read_text(encoding="utf-8").strip()

if not any(line.strip() and not line.lstrip().startswith("--") for line in query.splitlines()):
    raise SystemExit("Write a query in practice/sql/session_03/work.sql before running.")

try:
    with sqlite3.connect(":memory:") as connection:
        connection.executescript(setup)
        cursor = connection.execute(query)
        headers = [column[0] for column in cursor.description or ()]
        rows = cursor.fetchall()
except sqlite3.Error as exc:
    raise SystemExit(f"SQL error: {exc}") from exc

if headers:
    print(" | ".join(headers))
    print("-+-".join("-" * len(column) for column in headers))
for row in rows:
    print(" | ".join("NULL" if value is None else str(value) for value in row))
print(f"({len(rows)} rows)")
