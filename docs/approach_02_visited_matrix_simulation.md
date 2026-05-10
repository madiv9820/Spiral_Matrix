### Approach 02: Visited Matrix Simulation 🧭

### 💡 Intuition

Instead of shrinking boundaries, we can simulate a person walking through the matrix in spiral order.

The walker:

- keeps moving in the current direction
- turns when the next step goes out of bounds
- also turns when the next cell was already visited

To make that possible, we maintain a `visited` matrix. This gives us a very direct simulation of spiral movement and makes the turn logic easy to understand.

### 🧾 Pseudocode

```text
create empty result
create visited matrix filled with false

define directions in this order:
right, down, left, up

set current row = 0
set current col = 0
set current direction = right

repeat until all cells are visited:
    add current cell to result
    mark current cell as visited

    compute next row and next col using current direction

    if next position is out of bounds or already visited:
        rotate to the next direction
        recompute next row and next col

    move to next row and next col

return result
```

### ⏱️ Time Complexity

- ⏱️ `O(m * n)`

Each cell is added to the answer once.

### 📦 Space Complexity

- 📦 `O(m * n)`

The extra `visited` matrix stores one boolean value for every cell.
