# LeetCode Solutions

A growing collection of Python solutions used to practise algorithms, data structures, computational thinking, and performance-aware problem solving. Each exercise folder contains a `Task.md` brief and a notebook showing the implementation, examples, and—in several cases—the progression between approaches.

## Highlights

### [934. Shortest Bridge](<Tier 2/934 - Shortest Bridge/Solution.ipynb>)

The solution first discovers and marks one island, then uses breadth-first search to expand across the water one layer at a time. Reaching the second island at the earliest BFS layer gives the minimum number of flips. This showcases grid traversal, DFS/BFS selection, queue discipline, state marking, and shortest-path reasoning.

### [3372. Maximize the Number of Target Nodes After Connecting Trees](<Tier 2/3372 - Maximize No. of Target Nodes After Connecting Trees/solution.ipynb>)

The two trees are represented with adjacency lists and explored with a reusable distance-limited BFS helper. The best contribution from the second tree is combined with the reachable-node count for each starting node in the first. This demonstrates graph modelling, bounded traversal, helper-function design, and combining independent subproblem results.

### [112. Path Sum](<Tier 1/112 - Path Sum/solution.ipynb>)

The notebook records an initial exhaustive approach, identifies its memory limitation, and replaces it with an iterative depth-first traversal that carries each path’s running sum. Beyond tree traversal, this showcases profiling through failure, recognising unnecessary state, and improving an algorithm’s space complexity.

### [20. Valid Parentheses](<Tier 1/20 - Valid Parenthesis/solution.ipynb>)

A stack-based validation exercise for matching nested delimiters. It demonstrates choosing a data structure whose last-in, first-out behaviour directly models the problem and handling malformed input safely.

## Topics Practised

- Arrays, strings, dictionaries, sets, and frequency counting
- Stacks, two-pointer techniques, and sliding-window-style aggregation
- Binary trees, general trees, adjacency lists, DFS, and BFS
- Sorting, filtering, comprehensions, and incremental optimisation
- Complexity awareness, boundary cases, and example-driven verification

## Problem Index

### Tier 1 — Foundations

| Problem | Main focus |
|---|---|
| [1. Two Sum](<Tier 1/1 - two_sum/>) | Array search and complements |
| [13. Roman to Integer](<Tier 1/13 - roman_to_integer/>) | Mapping and string parsing |
| [14. Longest Common Prefix](<Tier 1/14 - longest_common_prefix/>) | Prefix comparison |
| [20. Valid Parentheses](<Tier 1/20 - Valid Parenthesis/>) | Stack-based validation |
| [26. Remove Duplicates from Sorted Array](<Tier 1/26 - Remove Duplicates from sorted Array/>) | In-place array processing |
| [112. Path Sum](<Tier 1/112 - Path Sum/>) | Iterative tree traversal |
| [884. Uncommon Words from Two Sentences](<Tier 1/884 - Uncommon Words from Two Sentences/>) | Token frequency counting |
| [1385. Distance Value Between Two Arrays](<Tier 1/1385 - Distance Value Between Two Arrays/>) | Pairwise comparison |
| [1556. Detect Pattern of Length M Repeated K Times](<Tier 1/1556 - Detect Pattern of Length M Repeated K Times/>) | Subarray pattern detection |
| [1588. Sum of All Odd Length Subarrays](<Tier 1/1588 - Sum All Odd Length Arrays/>) | Subarray aggregation |
| [1598. Crawler Log Folder](<Tier 1/1598 - Crawler Log Folder/>) | State tracking |
| [1704. Determine if String Halves Are Alike](<Tier 1/1704 - Determine if String Halves Alike/>) | String slicing and counting |
| [1880. Check if Word Equals Summation of Two Words](<Tier 1/1880 - Check if word Equals Two Word Summation/>) | Character-to-number conversion |
| [2057. Smallest Index With Equal Value](<Tier 1/2057 - Smallest Index with Equal Value/>) | Linear scanning |
| [2176. Count Equal and Divisible Pairs](<Tier 1/2176 - Count Equal & Divisible Pairs in Array/>) | Pair enumeration |
| [2231. Largest Number After Digit Swaps by Parity](<Tier 1/2231 - Largest Number After Digit Swaps by Parity/>) | Sorting under constraints |
| [2347. Best Poker Hand](<Tier 1/2347 - Best Poker Hand/>) | Frequency-based classification |
| [2553. Separate the Digits in an Array](<Tier 1/2553 - Separate Digits in Array/>) | Array transformation |
| [3318. Find X-Sum of All K-Long Subarrays I](<Tier 1/3318 - Find X-Sum of All K-Long Subarrays 1/>) | Frequency sorting and windows |

### Tier 2 — Graphs and Trees

| Problem | Main focus |
|---|---|
| [934. Shortest Bridge](<Tier 2/934 - Shortest Bridge/>) | Grid traversal and multi-source BFS |
| [3372. Maximize Target Nodes After Connecting Trees](<Tier 2/3372 - Maximize No. of Target Nodes After Connecting Trees/>) | Adjacency lists and bounded BFS |

## Progress

The tiers describe the learning progression within this repository rather than LeetCode’s official difficulty labels. New problems will be added as the collection expands into more advanced graph, dynamic-programming, and optimisation topics.
