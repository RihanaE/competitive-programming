class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        candidate = deque()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        stop = False
        temp = []
        
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(rw, cl):
            for i, j in direction:
                nw_rw = rw + i
                nw_cl = cl + j
                
                
                
                if inbound(nw_rw, nw_cl) and grid[nw_rw][nw_cl] == 1 and (nw_rw, nw_cl) not in visited:
                    visited.add((nw_rw, nw_cl))
                    temp.append((nw_rw, nw_cl))
                    dfs(nw_rw, nw_cl)
        
        
        for row in range(len(grid)):
            if not stop:
                for col in range(len(grid[0])):
                    flag = True
                    if grid[row][col] == 1:
                        # for i, j in direction:
                        #     nw_r = row + i
                        #     nw_c = col + j

                            # if inbound(nw_r, nw_c) and grid[nw_r][nw_c] == 1:
                                # flag = False
                            visited.add((row, col))
                            temp.append((row, col))
                            dfs(row, col)
                            candidate.append((temp, 0))
                            print(temp)
                            visited.add((row, col))
                            stop = True

                          
                            break

#                         if flag:
#                             # visited.add((row, col))
#                             # temp.append((row, col))
#                             # dfs(row, col)
#                             # candidate.append((temp, 0))
#                             # print(temp)
#                             # visited.add((row, col))
#                             # stop = True

#                             break
                        
        
        print(temp)
        
        def bfs():
            
            while candidate:
                node, no = candidate.popleft()
                temp1 = []
                
                for r, w in node:
                    rw, cl = r, w
           
                    for i, j in direction:
                        nw_rw, nw_cl = rw + i, cl + j

                        if inbound(nw_rw, nw_cl) and (nw_rw, nw_cl) not in visited and grid[nw_rw][nw_cl] == 1:
                            return no

                        elif inbound(nw_rw, nw_cl) and (nw_rw, nw_cl) not in visited and grid[nw_rw][nw_cl] == 0:
                            temp1.append((nw_rw, nw_cl))
                            # candidate.append((nw_rw, nw_cl, no + 1))
                            visited.add((nw_rw, nw_cl))
                            
                if temp1:
                    candidate.append((temp1, no + 1))
                        
        return bfs()