"""Run SQL Session 02 against a fresh in-memory SQLite database.

From the Programming repository root:
    python practice/sql/session_02/run.py
"""
from pathlib import Path
import sqlite3

directory = Path(__file__).resolve().parent
setup = (directory / "setup.sql").read_text(encoding="utf-8")
query = (directory / "work.sql").read_text(encoding="utf-8").strip()

if not any(line.strip() and not line.lstrip().startswith("--") for line in query.splitlines()):
    raise SystemExit("Write your SELECT query in practice/sql/session_02/work.sql first.")

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
    print("-+-".join("-" * len(header) for header in headers))
for row in rows:
    print(" | ".join(str(value) if value is not None else "NULL" for value in row))
print(f"({len(rows)} rows)")
