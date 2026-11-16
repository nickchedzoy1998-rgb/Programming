# Python algorithms — Session 02

## Challenge: Shortest qualifying segment

Write a function that receives a positive integer `target` and a list of **positive integers** `numbers`.

Return the **length of the shortest contiguous subarray** whose sum is **at least** `target`. Return `0` if no qualifying subarray exists.

A *contiguous* subarray consists of neighbouring elements; you cannot skip elements.

### Function contract

```python
def min_subarray_length(target: int, numbers: list[int]) -> int:
    ...
```

### Examples

| `target` | `numbers` | Expected result |
| ---: | --- | ---: |
| 7 | `[2, 3, 1, 2, 4, 3]` | 2 |
| 4 | `[1, 4, 4]` | 1 |
| 11 | `[1, 1, 1, 1, 1, 1, 1, 1]` | 0 |
| 3 | `[]` | 0 |

The input list may be empty. All elements of a nonempty `numbers` list and the `target` are strictly positive.

### Instructions

1. Write your implementation **only** in `solution.py`.
2. From the root of the Programming repository, run:

```powershell
python practice/algorithms/session_02/run.py
```

3. Send your attempt for code review, including any tests you struggled with.

Aim for **20–25 minutes**, then we will assess correctness, worst-case complexity and edge cases. Try it without searching for a solution. The tests do not reveal an implementation.
