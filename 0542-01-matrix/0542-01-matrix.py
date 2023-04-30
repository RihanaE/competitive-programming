class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        zeros = []
        ans = [[0] * len(mat[0]) for i in range(len(mat))]
        visited = set()
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    zeros.append((row, col))
                    
        def inbound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = deque()
        seen = set()
        
        for i in zeros:
            queue.append((i, 0))
            visited.add(i)
            seen.add(i)
        
        while queue:
            node, val = queue.popleft()
            
            if mat[node[0]][node[1]] == 1 and node not in seen:
                ans[node[0]][node[1]] = val
                seen.add(node)
              
            if len(seen) == len(mat) * len(mat[0]):
                break
                
            for r, c in directions:
                nw_r = node[0] + r
                nw_c = node[1] + c
                
                if inbound(nw_r, nw_c) and (nw_r, nw_c) not in visited:
                    queue.append(((nw_r, nw_c), val + 1))
                    visited.add((nw_r, nw_c))
                    
        return ans