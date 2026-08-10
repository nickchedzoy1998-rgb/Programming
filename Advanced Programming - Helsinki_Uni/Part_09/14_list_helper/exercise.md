# Exercise

Create a class named `ListHelper` with the following two class methods:

- `greatest_frequency(my_list: list)` — returns the most common item in the list.
- `doubles(my_list: list)` — returns the number of unique items that appear at least twice in the list.

The methods should be usable without creating an instance of the class.

## Example

```python
numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
```

## Sample output

```text
5
3
```