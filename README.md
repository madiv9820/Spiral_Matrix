# [Spiral Matrix 🌀](https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150)

### 📘 Problem

Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

### ❓ What Is The Question Asking?

You are given a 2D grid of numbers, and your task is to list them in the order you would see if you walked around the matrix in a spiral:

- ➡️ left to right across the top
- ⬇️ top to bottom down the right side
- ⬅️ right to left across the bottom
- ⬆️ bottom to top up the left side

Then you keep repeating that pattern, moving inward, until every element has been visited.

### 🧪 Example 1

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

**Input**
```text
matrix = [[1,2,3],[4,5,6],[7,8,9]]
```

**Output**
```text
[1,2,3,6,9,8,7,4,5]
```

### 🧪 Example 2

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

**Input**
```text
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
```

**Output**
```text
[1,2,3,4,8,12,11,10,9,5,6,7]
```

### 📏 Constraints

- **`m == matrix.length`**
- **`n == matrix[i].length`**
- **`1 <= m, n <= 10`**
- **`-100 <= matrix[i][j] <= 100`**

### 📚 Approach Notes

Detailed explanations for each implementation live in the [`docs/`](./docs) folder 📂

| Approach | Idea | Time | Extra Space | Notes |
| --- | --- | --- | --- | --- |
| [**🌀 Boundary Shrinking**](./docs/approach_01_boundary_shrinking.md) | Repeatedly traverse the current outer rectangle, then shrink the boundaries inward. | `O(m * n)` | `O(1)` | Great when you want a compact in-place traversal with no visited grid. |
| [**🧭 Visited Matrix Simulation**](./docs/approach_02_visited_matrix_simulation.md) | Simulate spiral movement step by step and turn whenever the next cell is invalid or already visited. | `O(m * n)` | `O(m * n)` | Easiest to visualize because it behaves like an actual walk through the matrix. |
| [**🎯 Layer By Layer**](./docs/approach_03_layer_by_layer.md) | Process one full ring at a time by collecting top, right, bottom, and left edges. | `O(m * n)` | `O(1)` | Clean and structured when you want to think in complete layers. |
---
