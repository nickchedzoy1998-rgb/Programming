
### Begin with a vowel

Write a function named `begin_with_vowel(words: list)` which takes a list of strings as its argument.

The function should use a list comprehension to create and return a new list containing only those words from the original list which begin with a vowel (`a`, `e`, `i`, `o`, `u`). Both lowercase and uppercase letters should be accepted.

- The function must be no longer than two lines of code, including the `def` line.

The function should work as follows:

```python
word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
	print(vowelled)
```

Sample output:

```
automobile
Animal
APPLE
orange
```
