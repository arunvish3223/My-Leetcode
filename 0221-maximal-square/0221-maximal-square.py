from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        side = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    if i < m-1 and j < n-1:
                        matrix[i][j] = 1 + min(int(matrix[i][j+1]), int(matrix[i+1][j]), int(matrix[i+1][j+1]))
                    side = max(side, int(matrix[i][j]))     
        return side * side
