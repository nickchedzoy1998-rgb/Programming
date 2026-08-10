### Rows of stars

Write a function named `rows_of_stars(numbers: list)` which takes a list of integers as its argument and returns a new list containing rows of stars. The length of each row should correspond to the integer at the same index in the original list.

- Use a list comprehension.
- The function must be no longer than two lines of code, including the `def` line.

The function should work as follows:

```python
rows = rows_of_stars([1, 2, 3, 4])
for row in rows:
    print(row)

print()

rows = rows_of_stars([4, 3, 2, 1, 10])
for row in rows:
    print(row)
```

Sample output:

```
*
**
***
****

****
***
**
*
**********
```
