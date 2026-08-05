# Sort by number of seasons

Write a function named `sort_by_seasons(items: list)` that accepts a list of
dictionaries. Each dictionary represents a TV show with the keys `name`,
`rating` and `seasons`.

Requirements:

- Return a *new list* sorted by the number of seasons (ascending).
- Do not modify the original input list.

Function signature:

```python
def sort_by_seasons(items: list) -> list:
    """Return a new list of shows sorted by number of seasons (ascending)."""
    ...
```

Example:

```python
shows = [
    {"name": "Dexter", "rating": 8.6, "seasons": 9},
    {"name": "Friends", "rating": 8.9, "seasons": 10},
    {"name": "Simpsons", "rating": 8.7, "seasons": 32},
]

for show in sort_by_seasons(shows):
    print(f"{show['name']} {show['seasons']} seasons")
```

Sample output:

```
Dexter 9 seasons
Friends 10 seasons
Simpsons 32 seasons
```

Notes:

- The `sorted()` built-in with a `key` such as `lambda s: s['seasons']` is
  suitable here.