# 1. Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two values whose sum equals `target`.

Each input has exactly one solution. The same array element cannot be used twice, and the indices may be returned in either order.

## Examples

```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

```text
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

```text
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

## Goal

Use the relationship between a value and its required complement to locate the pair without reusing an index.
