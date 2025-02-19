from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r1, c1):
            nonlocal island 
            visit.add((r1, c1))
            q = deque([(r1, c1)])
            
            while q:
                r, c = q.popleft()
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (0 <= row < rows and 0 <= col < cols and 
                        grid[row][col] == '1' and (row, col) not in visit):
                        q.append((row, col))
                        visit.add((row, col))
            island += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)

        return island
