### Approach 01: Boundary Shrinking 🌀

### 💡 Intuition

The spiral order always comes from the current outer rectangle of the matrix:

- ➡️ top row
- ⬇️ right column
- ⬅️ bottom row
- ⬆️ left column

After finishing those four sides, that outer layer is complete. So instead of tracking visited cells, we can simply shrink the rectangle inward and repeat the same process on the remaining inner matrix.

This works well because every spiral layer is just a smaller version of the same shape.

### 🧾 Pseudocode

```text
create empty result

set rowStart = 0
set rowEnd = last row index
set colStart = 0
set colEnd = last column index

while rowStart <= rowEnd and colStart <= colEnd:
    traverse top row from colStart to colEnd
    rowStart += 1

    if boundaries are invalid:
        stop

    traverse right column from rowStart to rowEnd
    colEnd -= 1

    if boundaries are invalid:
        stop

    traverse bottom row from colEnd down to colStart
    rowEnd -= 1

    if boundaries are invalid:
        stop

    traverse left column from rowEnd down to rowStart
    colStart += 1

return result
```

### ⏱️ Time Complexity

- ⏱️ `O(m * n)`

Every cell is visited exactly once.

### 📦 Space Complexity

- 📦 `O(1)` extra space

The boundary pointers use constant extra memory. The output list is not counted as extra auxiliary space.
