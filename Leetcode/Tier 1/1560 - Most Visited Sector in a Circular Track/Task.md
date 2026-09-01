# 1560. Most Visited Sector in a Circular Track

## Problem

Given an integer `n` and an integer array `rounds`, there is a circular track consisting of `n` sectors labeled from `1` to `n`. A marathon consists of `m` rounds. The i-th round starts at sector `rounds[i - 1]` and ends at sector `rounds[i]`. For example, round 1 starts at sector `rounds[0]` and ends at sector `rounds[1]`.

Return an array of the most visited sectors sorted in ascending order.

Note that you circulate the track in ascending order of sector numbers in the counter-clockwise direction.

---

## Examples

### Example 1

Input:

```
n = 4
rounds = [1, 3, 1, 2]
```

Output:

```
[1, 2]
```

Explanation:

The marathon starts at sector 1. The order of visited sectors is:

1 → 2 → 3 (end of round 1) → 4 → 1 (end of round 2) → 2 (end of round 3 and the marathon)

Sectors 1 and 2 are visited twice; sectors 3 and 4 are visited once.

### Example 2

Input:

```
n = 2
rounds = [2, 1, 2, 1, 2, 1, 2, 1, 2]
```

Output:

```
[2]
```

### Example 3

Input:

```
n = 7
rounds = [1, 3, 5, 7]
```

Output:

```
[1, 2, 3, 4, 5, 6, 7]
```

---

## Notes

- Sectors are labeled from `1` to `n`.
- The `rounds` array has length `m + 1` where `m` is the number of rounds (each round has a start and an end in consecutive entries).
- Return the resulting list of most visited sector labels sorted in ascending order.
