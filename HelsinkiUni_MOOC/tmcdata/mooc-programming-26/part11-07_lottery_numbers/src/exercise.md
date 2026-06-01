
### Lottery numbers

NB: Some exercises have multiple parts and can earn points separately.

## LotteryNumbers matched

Please write a class named `LotteryNumbers` which takes the week number (an integer) and a list of seven integers as its constructor arguments. The list should contain the correct lottery numbers for the given week.

Write a method named `number_of_hits(numbers: list)` which takes a list of integers as its argument. The method should return the number of correct entries in the parameter list.

- Use a list comprehension inside the method.
- The method must be no longer than two lines of code, including the `def` line.

Example:

```python
week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
my_numbers = [1,4,7,11,13,19,24]

print(week5.number_of_hits(my_numbers))
```

Sample output:

```
3
```

## LotteryNumbers matched in place

Write a method named `hits_in_place(numbers)` which takes a list of seven integers as its argument and returns a new list of seven integers. The new list should contain only those items from the parameter list which match the week's correct numbers; matching values must remain at the same indexes as in the original list and all other indexes should contain `-1`.

- Use a list comprehension inside the method.
- The method must be no longer than two lines of code, including the `def` line.

Example:

```python
week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]

print(week8.hits_in_place(my_numbers))
```

Sample output:

```
[1, -1, -1, 10, -1, 20, 30]
```
