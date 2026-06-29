# 2231. Largest Number After Digit Swaps by Parity

## Problem

You are given a positive integer `num`. You may swap any two digits of `num` that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of `num` after any number of swaps.

## Examples

### Example 1

- Input: `num = 1234`
- Output: `3412`

**Explanation:**
- Swap the digit `3` with the digit `1` → `3214`
- Swap the digit `2` with the digit `4` → `3412`

Note that there may be other sequences of swaps, but `3412` is the largest possible number. You may not swap the digit `4` with the digit `1` because they have different parity.

### Example 2

- Input: `num = 65875`
- Output: `87655`

**Explanation:**
- Swap the digit `8` with the digit `6` → `85675`
- Swap the first digit `5` with the digit `7` → `87655`

Again, there may be other sequences of swaps, but `87655` is the largest possible number.

## Constraints

- `1 <= num <= 10^9`
