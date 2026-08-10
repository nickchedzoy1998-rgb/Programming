# Climbing areas

> The exercise template includes `ClimbingRoute` from the previous exercise
> and also defines a `ClimbingArea` class.
>
> Example setup:
>
> ```python
> ca1 = ClimbingArea("Olhava")
> ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
> ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
> ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))
>
> ca2 = ClimbingArea("Nummi")
> ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))
>
> ca3 = ClimbingArea("Nalkkila slab")
> ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
> ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
> ca3.add_route(ClimbingRoute("Piggy not likey", 12, "6B+"))
> ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))
>
> print(ca1)
> print(ca3.name, ca3.routes())
> print(ca3.hardest_route())
> ```
>
> Sample output:
>
> ```text
> Olhava, 3 routes, hardest 6B
> Nalkkila slab 4
> Smooth operator, length 9 metres, grade 7A
> ```

## Sort by number of routes

Write a function named `sort_by_number_of_routes(areas: list)` that returns a
new list of `ClimbingArea` objects sorted by the number of routes each area
contains, in ascending order.

Requirements:

- Return a *new list*.
- Do not modify the original `areas` list.

Example:

```python
# ca1, ca2 and ca3 declared as above
areas = [ca1, ca2, ca3]
for area in sort_by_number_of_routes(areas):
    print(area)
```

Sample output:

```text
Nummi, 1 routes, hardest 8C+
Olhava, 3 routes, hardest 6B
Nalkkila slab, 4 routes, hardest 7A
```

## Sort by the most difficult route

Write a function named `sort_by_most_difficult(areas: list)` that returns a new
list of `ClimbingArea` objects sorted by the most difficult route in each area
in descending order.

Requirements:

- Return a *new list*.
- Do not modify the original `areas` list.
- Sort by the hardest route in each climbing area.

Example:

```python
# ca1, ca2 and ca3 declared as above
areas = [ca1, ca2, ca3]
for area in sort_by_most_difficult(areas):
    print(area)
```

Sample output:

```text
Nummi, 1 routes, hardest 8C+
Nalkkila slab, 4 routes, hardest 7A
Olhava, 3 routes, hardest 6B
```
