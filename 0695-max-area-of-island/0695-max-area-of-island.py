class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def helper(sr, sc):
            nonlocal count
            nonlocal res
            
            res = max(res, count)
            for r, c in direction:
                nw_r = sr + r
                nw_c = sc + c
                
                if inbound(nw_r, nw_c) and grid[nw_r][nw_c] == 1 and (nw_r, nw_c) not in visited:
                    visited.add((nw_r, nw_c))
                    count += 1
                    helper(nw_r, nw_c)
        
        
        
            
           
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        res = 0
        visited = set()
        
        for row in range(len(grid)):
                for col in range(len(grid[0])):
                    count = 0
                    if grid[row][col] == 1 and (row, col) not in visited:
                        visited.add((row, col))
                        count += 1
                        
                        helper(row, col)
        
        return res