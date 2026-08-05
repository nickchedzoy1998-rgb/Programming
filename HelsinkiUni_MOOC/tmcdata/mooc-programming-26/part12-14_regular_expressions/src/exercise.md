# Regular expressions

> **NB:** Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing **Submit Solution** from the menu next to the button for executing tests.

Here are some exercises for familiarizing yourself with regular expression syntax.

## Days of the week

Using a regular expression, please write a function named `is_dotw(my_string: str)`. The function should return `True` if the string passed as an argument contains an abbreviation for a day of the week (`Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat`, `Sun`).

Some examples of how the function should work:

```python
print(is_dotw("Mon"))
print(is_dotw("Fri"))
print(is_dotw("Tui"))
```

**Sample output**

```text
True
True
False
```

## Check for vowels

Please write a function named `all_vowels(my_string: str)` which uses a regular expression to check whether all characters in the given string are vowels.

Some examples of how the function should work:

```python
print(all_vowels("eioueioieoieou"))
print(all_vowels("autoooo"))
```

**Sample output**

```text
True
False
```

## Time of day

Please write a function named `time_of_day(my_string: str)` which uses a regular expression to check whether a string in the format `XX:YY:ZZ` is a valid time in the 24-hour format, with two digits each for hours, minutes and seconds.

Some examples of how the function should work:

```python
print(time_of_day("12:43:01"))
print(time_of_day("AB:01:CD"))
print(time_of_day("17:59:59"))
print(time_of_day("33:66:77"))
```

**Sample output**

```text
True
False
True
False
```
