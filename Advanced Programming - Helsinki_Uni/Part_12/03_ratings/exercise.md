# Sort by ratings

Write a function named `sort_by_ratings(items: list)` that accepts a list of
TV show dictionaries. Each dictionary contains the same structure as the
previous exercise: `name`, `rating`, and `seasons`.

Requirements:

- The function returns a *new list* of dictionaries sorted by rating in
  descending order.
- The original input list must not be modified.

Function signature:

```python
def sort_by_ratings(items: list) -> list:
    """Return a new list of shows sorted by rating, highest first."""
    ...
```

Example:

```python
shows = [
    {"name": "Dexter", "rating": 8.6, "seasons": 9},
    {"name": "Friends", "rating": 8.9, "seasons": 10},
    {"name": "Simpsons", "rating": 8.7, "seasons": 32},
]

print("Rating according to IMDB")
for show in sort_by_ratings(shows):
    print(f"{show['name']} {show['rating']}")
```

Sample output:

```
Rating according to IMDB
Friends 8.9
Simpsons 8.7
Dexter 8.6
```

Notes:

- Use the `sorted()` built-in with `reverse=True` and a key like
  `lambda show: show['rating']`.
