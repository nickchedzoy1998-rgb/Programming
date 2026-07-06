# 2176. Count Equal and Divisible Pairs in an Array

Given a 0-indexed integer array `nums` of length `n` and an integer `k`, return the number of pairs `(i, j)` where `0 <= i < j < n`, such that `nums[i] == nums[j]` and `(i * j)` is divisible by `k`.

## Examples

**Example 1**

Input:

```
nums = [3, 1, 2, 2, 2, 1, 3], k = 2
```

Output: `4`

Explanation:

- `nums[0] == nums[6]`, and `0 * 6 == 0`, divisible by `2`.
- `nums[2] == nums[3]`, and `2 * 3 == 6`, divisible by `2`.
- `nums[2] == nums[4]`, and `2 * 4 == 8`, divisible by `2`.
- `nums[3] == nums[4]`, and `3 * 4 == 12`, divisible by `2`.

**Example 2**

Input:

```
nums = [1, 2, 3, 4], k = 1
```

Output: `0`

Explanation: No repeated values in `nums`, so no valid pairs exist.

## Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i], k <= 100`

---

Generated: improved formatting for readability. No problem statement changes were made.