# 1598. Crawler Log Folder

The LeetCode file system keeps a log each time a user performs a change-folder operation.

## Operations

- `../` : Move to the parent folder of the current folder. If already in the main folder, remain there.
- `./`  : Remain in the same folder.
- `x/`  : Move to the child folder named `x` (the folder is guaranteed to exist).

You are given an array of strings `logs` where `logs[i]` is the operation performed by the user at the i-th step. The file system starts in the main folder and the operations are executed in order.

Return the minimum number of operations required to return to the main folder after performing all operations in `logs`.

## Examples

**Example 1**

Input:

```
logs = ["d1/", "d2/", "../", "d21/", "./"]
```

Output: `2`

Explanation: Use the operation `../` twice to return to the main folder.

**Example 2**

Input:

```
logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
```

Output: `3`

**Example 3**

Input:

```
logs = ["d1/", "../", "../", "../"]
```

Output: `0`

## Constraints

- `1 <= logs.length <= 10^3`
- `2 <= logs[i].length <= 10`
- `logs[i]` contains lowercase English letters, digits, `.` and `/`.
- `logs[i]` follows the format described above; folder names consist of lowercase letters and digits.
