"""Run the SQL query in work.sql against fresh sample data.

From the Programming repository root:
    python practice/sql/session_01/run.py
"""
from pathlib import Path
import sqlite3

folder = Path(__file__).resolve().parent
setup = (folder / "setup.sql").read_text(encoding="utf-8")
query = (folder / "work.sql").read_text(encoding="utf-8").strip()

if not any(line.strip() and not line.lstrip().startswith("--") for line in query.splitlines()):
    raise SystemExit("Open practice/sql/session_01/work.sql and write your SELECT query first.")

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
    print(" | ".join(str(value) if value is not None else "NULL" for value in row))
print(f"({len(rows)} rows)")
