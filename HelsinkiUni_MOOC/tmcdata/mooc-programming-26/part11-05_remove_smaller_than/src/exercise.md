
### Remove smaller than

Write a function named `remove_smaller_than(numbers: list, limit: int)` which takes a list of integers and a limit value (also an integer) as its arguments.

The function should use a list comprehension to produce a new list without the values which are smaller than the limit value.

- The function must be no longer than two lines of code, including the `def` line.

The function should work as follows:

```python
numbers = [1, 65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))
```

Sample output:

```
[65, 32, 11]
[7, 8]
```
