# 1880. Check if Word Equals Summation of Two Words

## Problem

Given three strings firstWord, secondWord, and targetWord (each consisting of lowercase letters 'a' to 'j'), determine whether the numerical value of targetWord equals the sum of the numerical values of firstWord and secondWord.

## Definitions
- Letter value: position in the alphabet starting from 0 (a -> 0, b -> 1, ..., j -> 9).
- Numerical value of a string s: concatenate the letter values of each character in s, then convert the concatenation to an integer.

Example: s = "acb" -> letter values "0","2","1" -> concatenation "021" -> integer 21.

## Return
Return true if numerical_value(firstWord) + numerical_value(secondWord) == numerical_value(targetWord), otherwise return false.

## Examples

1) Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"

	Output: true

	Explanation:
	- firstWord: "acb" -> "021" -> 21
	- secondWord: "cba" -> "210" -> 210
	- targetWord: "cdb" -> "231" -> 231
	- 21 + 210 == 231

2) Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"

	Output: false

	Explanation:
	- firstWord: "aaa" -> "000" -> 0
	- secondWord: "a" -> "0" -> 0
	- targetWord: "aab" -> "001" -> 1
	- 0 + 0 != 1

3) Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"

	Output: true

	Explanation:
	- firstWord: "aaa" -> "000" -> 0
	- secondWord: "a" -> "0" -> 0
	- targetWord: "aaaa" -> "0000" -> 0
	- 0 + 0 == 0

## Constraints

- 1 <= firstWord.length, secondWord.length, targetWord.length <= 8
- firstWord, secondWord, and targetWord consist of lowercase letters from 'a' to 'j' inclusive.