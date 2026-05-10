### Approach 03: Layer By Layer 🎯

### 💡 Intuition

This approach treats the matrix like a set of concentric layers.

For each layer, we collect:

- ➡️ the top edge
- ⬇️ the right edge
- ⬅️ the bottom edge
- ⬆️ the left edge

Once a full ring is processed, we move inward to the next layer by shrinking all four boundaries together.

This is close to the boundary-shrinking idea, but the implementation is organized more explicitly around finishing one full layer at a time.

### 🧾 Pseudocode

```text
create empty result

set rowStart = 0
set rowEnd = last row index
set colStart = 0
set colEnd = last column index

while rowStart <= rowEnd and colStart <= colEnd:
    traverse top edge from left to right
    traverse right edge from top+1 to bottom

    if there is a distinct bottom row:
        traverse bottom edge from right-1 to left

    if there is a distinct left column:
        traverse left edge from bottom-1 to top+1

    rowStart += 1
    rowEnd -= 1
    colStart += 1
    colEnd -= 1

return result
```

### ⏱️ Time Complexity

- ⏱️ `O(m * n)`

Every matrix element is processed once.

### 📦 Space Complexity

- 📦 `O(1)` extra space

Only boundary variables are used besides the output list.
