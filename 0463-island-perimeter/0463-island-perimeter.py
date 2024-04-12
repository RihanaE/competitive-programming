class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir_ = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        res = 0
        flag = False
        
        def isBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def count(row, col):
            num = 4
            
            for rw, cl in dir_:
                nw_rw, nw_cl = rw + row, cl + col
                if isBound(nw_rw, nw_cl) and grid[nw_rw][nw_cl] == 1:
                    num -= 1
                    
            return num
        
        for rw in range(len(grid)):
            for cl in range(len(grid[0])):
                if grid[rw][cl] == 1:
                    stack = [[rw, cl]]
                    visited.add((rw, cl))
                    flag = True
                    break
                    
            if flag:
                break
                
       
        while stack:
            row, col = stack.pop()
            res += count(row, col)
            
            for i, j in dir_:
                nw_row, nw_col = row + i, col + j
                
                if (nw_row, nw_col) not in visited and isBound(nw_row, nw_col) and grid[nw_row][nw_col] == 1:
                    stack.append([nw_row, nw_col])
                    visited.add((nw_row, nw_col))
                    
        return res