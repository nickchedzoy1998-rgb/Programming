# Sort by remaining stock

Write a function named `sort_by_remaining_stock(items: list)` that accepts a list of
tuples. Each tuple describes a product as `(name, price, remaining_stock)`.

Requirements:

- The function returns a *new list* with the items sorted by the remaining stock
  (lowest first).
- The original list must not be modified.

Function signature:

```python
def sort_by_remaining_stock(items: list) -> list:
    """Return a new list of items sorted by remaining stock (ascending)."""
    ...
```

Example:

```python
products = [
    ("banana", 5.95, 12),
    ("apple", 3.95, 3),
    ("orange", 4.50, 2),
    ("watermelon", 4.95, 22),
]

for product in sort_by_remaining_stock(products):
    print(f"{product[0]} {product[2]} pcs")
```

Sample output:

```
orange 2 pcs
apple 3 pcs
banana 12 pcs
watermelon 22 pcs
```

Notes:

- The function should not modify the input list; return a new sorted list instead.
- You can use the `sorted()` built-in with an appropriate `key` function.