class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance, 0)])
        visited = set([(entrance[0], entrance[1])])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def inbound(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        
        
        while queue:
            node, res = queue.popleft()
            
    
            
            for r, c in directions:
                nw_r = r + node[0]
                nw_c = c + node[1]
                
                if not inbound(nw_r, nw_c) and [node[0], node[1]] != entrance:
                    return res
                
                if inbound(nw_r, nw_c) and (nw_r, nw_c) not in visited and maze[nw_r][nw_c] != '+':
                    queue.append(((nw_r, nw_c), res + 1))
                    visited.add((nw_r, nw_c))
                    
        return -1