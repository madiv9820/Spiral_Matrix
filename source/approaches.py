"""📚 Collection of Spiral Matrix approach implementations.

This file stores multiple traversal strategies so the main solution
can switch between them without changing the public interface.
"""

from typing import List, Tuple

class Approaches:
    def _approach_01_boundary_shrinking(self) -> List[int]:
        # 🌀 Build the answer by repeatedly traversing the outer layer
        # of the matrix, then shrinking the remaining boundaries inward.
        result: List[int] = []

        def is_valid() -> bool:
            # ✅ The current window is valid only if there are still rows
            # and columns left to visit inside the shrinking rectangle.
            return rowStart <= rowEnd and colStart <= colEnd

        # 📦 These pointers track the current unvisited rectangle:
        # `rowStart` / `rowEnd` for the top and bottom edges,
        # `colStart` / `colEnd` for the left and right edges.
        rowStart:   int = 0
        rowEnd:     int = len(self._matrix) - 1
        colStart:   int = 0
        colEnd:     int = len(self._matrix[0]) - 1

        while True:
            if not is_valid():
                break

            # ➡️ Traverse the top row of the current layer.
            # After this pass, every element on `rowStart` has been collected.
            for position in range(colStart, colEnd + 1):
                result.append(self._matrix[rowStart][position])
            
            # ⬇️ Move the top boundary down so it is not visited again.
            rowStart += 1

            if not is_valid():
                break

            # ⬇️ Traverse the rightmost column of the remaining layer.
            # We start from the updated `rowStart` to avoid repeating the corner
            # that was already taken in the top-row traversal.
            for position in range(rowStart, rowEnd + 1):
                result.append(self._matrix[position][colEnd])
            
            # ⬅️ Move the right boundary left so it is excluded next time.
            colEnd -= 1
            
            if not is_valid():
                break
            
            # ⬅️ Traverse the bottom row of the current layer in reverse order.
            # This collects the lower edge without touching any cell twice.
            for position in range(colEnd, colStart - 1, -1):
                result.append(self._matrix[rowEnd][position])
            
            # ⬆️ Move the bottom boundary up because that row is now finished.
            rowEnd -= 1

            if not is_valid():
                break

            # ⬆️ Traverse the leftmost column upward.
            # We stop at the updated `rowStart` so the top-left corner
            # from this layer is not added twice.
            for position in range(rowEnd, rowStart - 1, -1):
                result.append(self._matrix[position][colStart])
            
            # ➡️ Move the left boundary right and begin the next inner layer.
            colStart += 1

        return result

    def _approach_02_visited_matrix_simulation(self) -> List[int]:
        # 🌀 Simulate the spiral walk one step at a time.
        # We keep moving in the current direction until we either
        # leave the matrix or hit a cell that was already visited.
        result: List[int] = []

        # 📏 Basic matrix dimensions and the total number of cells
        # we must collect before the traversal is complete.
        totalRows:      int = len(self._matrix)
        totalCols:      int = len(self._matrix[0])
        totalCells:     int = totalRows * totalCols
        cellsVisited:   int = 0

        # ✅ Track which cells have already been added to the answer
        # so we know exactly when to turn to the next direction.
        visited: List[List[bool]] = [[False] * totalCols for _ in range(totalRows)]

        # 🧭 Direction order for spiral traversal:
        # right -> down -> left -> up.
        currentDirection:   int             = 0
        directions:         List[Tuple[int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

        # 🎬 Start from the top-left corner of the matrix.
        currentRow: int = 0
        currentCol: int = 0 

        while cellsVisited < totalCells:
            # 📥 Visit the current cell and record it in spiral order.
            result.append(self._matrix[currentRow][currentCol])
            visited[currentRow][currentCol] = True
            cellsVisited += 1

            # 🔭 Try to move one step forward in the current direction.
            nextRow: int = currentRow + directions[currentDirection][0]
            nextCol: int = currentCol + directions[currentDirection][1]

            if (
                    nextRow < 0 
                or  nextRow >= totalRows 
                or  nextCol < 0 
                or  nextCol >= totalCols 
                or  visited[nextRow][nextCol]
            ):
                # 🔄 If the next step goes out of bounds or reaches an
                # already-visited cell, rotate to the next spiral direction.
                currentDirection = (currentDirection + 1) % 4
                nextRow = currentRow + directions[currentDirection][0]
                nextCol = currentCol + directions[currentDirection][1]
            
            # 🚶 Move to the next valid cell and continue the simulation.
            currentRow = nextRow
            currentCol = nextCol

        return result

    def _approach_03_layer_by_layer(self) -> List[int]:
        # 🌀 Process the matrix one full outer layer at a time.
        # Each loop collects the top, right, bottom, and left edges,
        # then moves inward to the next smaller layer.
        result: List[int] = []

        # 📦 These boundaries describe the current layer we are traversing.
        rowStart:   int = 0
        rowEnd:     int = len(self._matrix) - 1
        colStart:   int = 0
        colEnd:     int = len(self._matrix[0]) - 1

        while rowStart <= rowEnd and colStart <= colEnd:
            # ➡️ Traverse the top edge of the current layer.
            for position in range(colStart, colEnd + 1):
                result.append(self._matrix[rowStart][position])

            # ⬇️ Traverse the right edge, starting one row below the top corner
            # so the top-right cell is not collected twice.
            for position in range(rowStart + 1, rowEnd + 1):
                result.append(self._matrix[position][colEnd])

            if rowStart < rowEnd:
                # ⬅️ Traverse the bottom edge in reverse order only when
                # the layer still has a distinct bottom row.
                for position in range(colEnd - 1, colStart - 1, -1):
                    result.append(self._matrix[rowEnd][position])
            
            if colStart < colEnd:
                # ⬆️ Traverse the left edge upward only when the layer
                # still has a distinct left column.
                # We stop before `rowStart` to avoid repeating corners.
                for position in range(rowEnd - 1, rowStart, -1):
                    result.append(self._matrix[position][colStart])
            
            # 🎯 Shrink all four boundaries to move to the next inner layer.
            rowStart    += 1
            rowEnd      -= 1
            colStart    += 1
            colEnd      -= 1

        return result
