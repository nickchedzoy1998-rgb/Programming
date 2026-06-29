# ClimbingRoute

> The exercise template includes a `ClimbingRoute` class with the
> properties `name`, `length`, and `grade`.
>
> Example:
>
> ```python
> route1 = ClimbingRoute("Edge", 38, "6A+")
> route2 = ClimbingRoute("Smooth operator", 11, "7A")
> route3 = ClimbingRoute("Synchro", 14, "8C+")
>
> print(route1)
> print(route2)
> print(route3.name, route3.length, route3.grade)
> ```
>
> Sample output:
>
> ```text
> Edge, length 38 metres, grade 6A+
> Smooth operator, length 11 metres, grade 7A
> Synchro 14 8C+
> ```

## Sort by length

Write a function named `sort_by_length(routes: list)` that returns a new list of
`ClimbingRoute` objects sorted by `length` from longest to shortest.

Requirements:

- Return a *new list*.
- Do not modify the original `routes` list.

Function signature:

```python
def sort_by_length(routes: list) -> list:
    """Return a new list of routes sorted by length, longest first."""
    ...
```

Example:

```python
r1 = ClimbingRoute("Edge", 38, "6A+")
 r2 = ClimbingRoute("Smooth operator", 11, "7A")
 r3 = ClimbingRoute("Synchro", 14, "8C+")
 r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]

for route in sort_by_length(routes):
    print(route)
```

Sample output:

```text
Edge, length 38 metres, grade 6A+
Synchro, length 14 metres, grade 8C+
Small steps, length 12 metres, grade 6A+
Smooth operator, length 11 metres, grade 7A
```

## Sort by difficulty

Write a function named `sort_by_difficulty(routes: list)` that returns a new
list of `ClimbingRoute` objects sorted by `grade` from hardest to easiest.
For routes with the same grade, the longer route should come first.

Requirements:

- Return a *new list*.
- Do not modify the original `routes` list.
- Sort by grade descending, then by length descending for equal grades.

Function signature:

```python
def sort_by_difficulty(routes: list) -> list:
    """Return a new list of routes sorted by difficulty."""
    ...
```

Example:

```python
r1 = ClimbingRoute("Edge", 38, "6A+")
 r2 = ClimbingRoute("Smooth operator", 11, "7A")
 r3 = ClimbingRoute("Synchro", 14, "8C+")
 r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]

for route in sort_by_difficulty(routes):
    print(route)
```

Sample output:

```text
Synchro, length 14 metres, grade 8C+
Smooth operator, length 11 metres, grade 7A
Edge, length 38 metres, grade 6A+
Small steps, length 12 metres, grade 6A+
```

### Hint

Python sorts tuples lexicographically by default, comparing the first item first,
then the second, and so on.

Example:

```python
my_list = [("a", 4), ("a", 2), ("b", 30), ("b", 0)]
print(sorted(my_list))
```

Sample output:

```text
[('a', 2), ('a', 4), ('b', 0), ('b', 30)]
```