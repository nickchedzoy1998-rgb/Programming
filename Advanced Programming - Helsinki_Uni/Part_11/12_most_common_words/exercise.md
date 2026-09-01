### Most common words

Please write a function named `most_common_words(filename: str, lower_limit: int)` which takes a filename and an integer value for a lower limit as its arguments. The function should return a dictionary containing the occurrences of the words which appear at least the number of times specified in the `lower_limit` parameter.

For example, if the function is used to process a file named *comprehensions.txt* with the following contents:

```
List comprehension is an elegant way to define and create lists based on existing lists.
List comprehension is generally more compact and faster than normal functions and loops for creating list.
However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
Remember, every list comprehension can be rewritten in for loop, but every for loop can't be rewritten in the form of list comprehension.
```

When the function is called with the arguments `most_common_words("comprehensions.txt", 3)` it should return:

Sample output:

```
{'comprehension': 4, 'is': 3, 'and': 3, 'for': 3, 'list': 4, 'in': 3}
```

**Important notes:**

- The case of letters affects the results. The words `List`, `lists` and `list` are each separate words. Only `list` (lowercase) has enough occurrences to make it to the returned dictionary.
- All inflected forms are unique words in this exercise.
- All punctuation should be removed before counting the occurrences of words.
- It is up to you to decide how to implement this. List and dictionary comprehensions are likely the easiest approach.
