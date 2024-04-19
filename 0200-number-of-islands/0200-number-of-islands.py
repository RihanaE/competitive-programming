class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        queue = deque()
        dir_ = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def bfs(node):
            queue = deque([node])
            
            while queue:
                rw, cl = queue.popleft()
                
                for r, c in dir_:
                    nw_r, nw_c = rw + r, cl + c
                    
                    if inBound(nw_r, nw_c) and (nw_r, nw_c) not in visited and grid[nw_r][nw_c] == "1":
                        visited.add((nw_r, nw_c))
                        queue.append([nw_r, nw_c])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    visited.add((row, col))
                    res += 1
                    bfs([row, col])
                    
        
                        
        return res