# 3318. Find X-Sum of All K-Long Subarrays I

## Problem

You are given an array `nums` of `n` integers and two integers `k` and `x`.

The x-sum of an array is calculated by the following procedure:

1. Count the occurrences of all elements in the array.
2. Keep only the occurrences of the top `x` most frequent elements.
   - If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
3. Calculate the sum of the resulting array.

Note that if an array has less than `x` distinct elements, its x-sum is the sum of the array.

Return an integer array `answer` of length `n - k + 1` where `answer[i]` is the x-sum of the subarray `nums[i..i + k - 1]`.

## Examples

### Example 1

Input:

```text
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
```

Output:

```text
[6,10,12]
```

Explanation:

- For subarray `[1, 1, 2, 2, 3, 4]`, only elements `1` and `2` are kept. Hence, `answer[0] = 1 + 1 + 2 + 2 = 6`.
- For subarray `[1, 2, 2, 3, 4, 2]`, only elements `2` and `4` are kept. Hence, `answer[1] = 2 + 2 + 2 + 4 = 10`.
- For subarray `[2, 2, 3, 4, 2, 3]`, only elements `2` and `3` are kept. Hence, `answer[2] = 2 + 2 + 2 + 3 + 3 = 12`.

### Example 2

Input:

```text
nums = [3,8,7,8,7,5]
k = 2
x = 2
```

Output:

```text
[11,15,15,15,12]
```

Explanation:

Since `k == x`, `answer[i]` is equal to the sum of the subarray `nums[i..i + k - 1]`.

## Constraints

- `1 <= n == nums.length <= 50`
- `1 <= nums[i] <= 50`
- `1 <= x <= k <= nums.length`