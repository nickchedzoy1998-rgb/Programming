# 934. Shortest Bridge

## Problem

An `n x n` binary grid contains exactly two islands. A `1` represents land, a `0` represents water, and land cells connect vertically or horizontally.

Return the smallest number of water cells that must be changed to land to connect the two islands.

## Examples

```text
Input: grid = [[0, 1], [1, 0]]
Output: 1
```

```text
Input: grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
Output: 2
```

```text
Input: grid = [[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,1,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1]]
Output: 1
```

## Goal

Mark one connected island, then expand outward across water in breadth-first layers until the second island is reached.
