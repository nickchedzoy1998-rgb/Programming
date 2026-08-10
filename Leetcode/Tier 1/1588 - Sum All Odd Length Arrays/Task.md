# 1588. Sum of All Odd Length Subarrays

## Problem

Given an array of positive integers, return the sum of every possible contiguous subarray whose length is odd.

A subarray is a contiguous sequence of one or more values from the original array.

## Examples

```text
Input: arr = [1, 4, 2, 5, 3]
Output: 58
```

The odd-length subarrays have lengths 1, 3, and 5; their combined total is 58.

```text
Input: arr = [1, 2]
Output: 3
```

```text
Input: arr = [10, 11, 12]
Output: 66
```

## Goal

Enumerate valid windows or calculate how often each value contributes to an odd-length subarray.
