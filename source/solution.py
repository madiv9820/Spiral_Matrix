"""🌀 Entry point for the Spiral Matrix solution.

This file connects the public LeetCode method to the available
approach implementations and makes it easy to switch between them.
"""

from typing import List
from .approaches import Approaches

class Solution(Approaches):
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self._matrix: List[List[int]] = matrix
        
        # return self._approach_01_boundary_shrinking()
        # return self._approach_02_visited_matrix_simulation()
        return self._approach_03_layer_by_layer()
