class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        direction = [(1, -1), (-1, 1), (1, 1), (1, 0),
                     (0, 1), (-1, 0), (-1, -1), (0, -1)]
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        queue = deque([(0, 0, 1)])
        res = 0
        visited = set((0,0))
        
        while queue:
            
            value = queue.popleft()
            
            if (value[0], value[1]) == (len(grid) - 1, len(grid[0]) - 1):
                res = value[-1]
                break
            
           
            for row, col in direction:
                nw_r = value[0] + row
                nw_c = value[1] + col
                
                
                if (nw_r, nw_c) not in visited and inbound(nw_r, nw_c):

                    if grid[nw_r][nw_c] == 0:
                        queue.append((nw_r, nw_c, value[2] + 1))
                        visited.add((nw_r, nw_c))
                
                
        if res == 0:
            return -1
        return res