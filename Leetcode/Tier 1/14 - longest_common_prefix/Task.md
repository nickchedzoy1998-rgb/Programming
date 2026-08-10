# 14. Longest Common Prefix

## Problem

Given an array of strings, return the longest prefix shared by every string. Return an empty string when there is no common prefix.

## Examples

```text
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
```

```text
Input: strs = ["dog", "racecar", "car"]
Output: ""
```

## Goal

Compare characters or progressively shorten a candidate prefix while safely handling strings of different lengths.
