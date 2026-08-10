# 13. Roman to Integer

## Problem

Convert a valid Roman numeral string to its integer value. Roman numerals normally list symbols from largest to smallest, but a smaller symbol placed before a larger one represents subtraction.

| Symbol | Value |
|---|---:|
| `I` | 1 |
| `V` | 5 |
| `X` | 10 |
| `L` | 50 |
| `C` | 100 |
| `D` | 500 |
| `M` | 1000 |

The subtractive pairs are `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`.

## Examples

```text
Input: s = "III"
Output: 3
```

```text
Input: s = "LVIII"
Output: 58
```

```text
Input: s = "MCMXCIV"
Output: 1994
```
