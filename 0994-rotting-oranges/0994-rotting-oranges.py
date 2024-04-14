class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir_ = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()
        candidate = []
        visited = set()
        num = 0
        time = 0
        
        def isBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        for rw in range(len(grid)):
            for cl in range(len(grid[0])):
                if grid[rw][cl] == 1:
                    num += 1
                    
                elif grid[rw][cl] == 2:
                    candidate.append([rw, cl])
                    visited.add((rw, cl))
                    
        queue.append(candidate)
        
        while queue:
            nodes = queue.popleft()
            temp = []
            
            for rw, cl in nodes:
                for i, j in dir_:
                    nw_rw, nw_cl = rw + i, cl + j
                    
                    if isBound(nw_rw, nw_cl) and (nw_rw, nw_cl) not in visited and grid[nw_rw][nw_cl] == 1:
                        num -= 1
                        visited.add((nw_rw, nw_cl))
                        temp.append([nw_rw, nw_cl])
            
            if temp:
                queue.append(temp)
                time += 1
                
            if num == 0:
                return time
            
        if num != 0:
            return -1
        
        else:
            return time