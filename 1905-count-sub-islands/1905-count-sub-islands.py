class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        count = 0
        
        def inbound(row, col):
            return 0 <= row < len(grid1) and 0 <= col < len(grid1[0])
        
        
        
        def dfs(rw, cl):
            nonlocal count
            nonlocal visited
            
            stack = [[rw, cl]]
            flag = False
            
            while stack:
                row, col = stack.pop()
                
                for r, c in directions:
                    nw_r = row + r
                    nw_c = col + c
                    
                    if inbound(nw_r, nw_c) and (nw_r, nw_c) not in visited and grid1[nw_r][nw_c] == 1 and grid2[nw_r][nw_c] == 1:
                        stack.append([nw_r, nw_c])
                        visited.add((nw_r, nw_c))
                        
                    elif inbound(nw_r, nw_c) and not flag and (nw_r, nw_c) not in visited and grid1[nw_r][nw_c] != 1 and grid2[nw_r][nw_c] == 1:
                        
                        visited.add((nw_r, nw_c))
                        stack.append([nw_r, nw_c])
                        count -= 1
                        flag = True
                    
                    elif inbound(nw_r, nw_c) and (nw_r, nw_c) not in visited and grid1[nw_r][nw_c] != 1 and grid2[nw_r][nw_c] == 1:
                        visited.add((nw_r, nw_c))
                        stack.append([nw_r, nw_c])
                        
                    # elif inbound(nw_r, nw_c):
                    #     visited.add((nw_r, nw_c))
        
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if (row, col) not in visited and grid1[row][col] == 1 and grid2[row][col] == 1:
                    count += 1
                    visited.add((row, col))
                    dfs(row, col)
                    
                    
        
                        
                        
        return count