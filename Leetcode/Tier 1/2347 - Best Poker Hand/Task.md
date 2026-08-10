# 2347. Best Poker Hand

## Problem

You are given five poker-card ranks and their corresponding suits. Return the best hand that can be formed under these rules:

- `Flush`: all five cards have the same suit.
- `Three of a Kind`: at least three cards share the same rank.
- `Pair`: at least two cards share the same rank.
- `High Card`: none of the stronger hands apply.

## Examples

```text
Input: ranks = [13, 2, 3, 1, 9], suits = ["a", "a", "a", "a", "a"]
Output: "Flush"
```

```text
Input: ranks = [4, 4, 2, 4, 4], suits = ["d", "a", "a", "b", "c"]
Output: "Three of a Kind"
```

```text
Input: ranks = [10, 10, 2, 12, 9], suits = ["a", "b", "c", "a", "d"]
Output: "Pair"
```

## Goal

Classify the hand by checking suit uniformity and rank frequencies in priority order.
