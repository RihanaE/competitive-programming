class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        flag = False
        dir_ = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ans = 0
        
        def isBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def count(row, col):
            res = 4
            for rw, cl in dir_:
                nw_rw, nw_cl = row + rw, col + cl
                
                if isBound(nw_rw, nw_cl) and grid[nw_rw][nw_cl] == 1:
                    res -= 1
                
            return res
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    queue.append([row, col])
                    visited.add((row, col))
                    flag = True
                    break
                    
            if flag:
                break
                
 
        while queue:
            row, col = queue.popleft()
            ans += count(row, col)
            
            for rw, cl in dir_:
                nw_rw, nw_cl = rw + row, col + cl
                
                if isBound(nw_rw, nw_cl) and (nw_rw, nw_cl) not in visited and grid[nw_rw][nw_cl] == 1:
                    queue.append([nw_rw, nw_cl])
                    visited.add((nw_rw, nw_cl))
        return ans