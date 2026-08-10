# 26. Remove Duplicates from Sorted Array

## Problem

Given an integer array `nums` sorted in non-decreasing order, remove duplicate values in place so that every unique value appears once. Preserve the relative order of the unique values.

Return the number `k` of unique values. After the operation, the first `k` positions in `nums` must contain those values; anything after index `k - 1` is irrelevant.

## Examples

```text
Input: nums = [1, 1, 2]
Output: k = 2, nums = [1, 2, _]
```

```text
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: k = 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```

## Goal

Use the array’s sorted order to identify changes and compact unique values without allocating a replacement array for the result.
