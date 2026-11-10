"""Run SQL practice against a fresh in-memory SQLite database.

Usage from the Programming repository root:
    python practice/sql/run_query.py

Edit answer_01.sql to write your solution; tables and seed records are
recreated from session_01.sql every time you run the script.
"""
from pathlib import Path
import sqlite3

HERE = Path(__file__).resolve().parent
setup = (HERE / "session_01.sql").read_text(encoding="utf-8")
answer = (HERE / "answer_01.sql").read_text(encoding="utf-8").strip()

if not answer or all(not line.strip() or line.lstrip().startswith("--") for line in answer.splitlines()):
    raise SystemExit("Write your query in practice/sql/answer_01.sql, then run this script again.")

with sqlite3.connect(":memory:") as db:
    db.executescript(setup)
    cursor = db.execute(answer)
    headings = [col[0] for col in cursor.description or []]
    rows = cursor.fetchall()

if headings:
    print(" | ".join(headings))
    print("-+-".join("-" * len(h) for h in headings))
for row in rows:
    print(" | ".join(str(value) for value in row))
print(f"({len(rows)} rows)")
