from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid2[r][c] == 0 or (r, c) in visited:
                return True
            visited.add((r, c))
            res = grid1[r][c] == 1
            res &= dfs(r + 1, c)
            res &= dfs(r - 1, c)
            res &= dfs(r, c + 1)
            res &= dfs(r, c - 1)
            return res

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    count += 1
                    
        return count