class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dir = [[1,0], [0,1], [-1,0], [0,-1]]
        
        keycount = 0
        q = deque()
        seen = set()
        
        for i in range(rows):
            for j in range(cols):
                
                if 'a' <= grid[i][j] <= 'z':
                    keycount += 1
                    
                if grid[i][j] == '@':
                    q.append((i,j,'',0)) 
                    seen.add((i,j,''))
                    
       
        while q:
            i,j,keys,steps = q.popleft()
           
            if len(keys) == keycount:
                return steps
            
            for rw,cl in dir:
                ni = i + rw
                nj = j + cl
                
                if 0<=ni<rows and 0<=nj<cols and grid[ni][nj] != '#' and (ni,nj,keys) not in seen:
                    
                    if grid[ni][nj] in "@." or grid[ni][nj].lower() in keys:
                        q.append((ni,nj, keys, steps+1))
                        seen.add((ni, nj, keys))
                        
                    elif 'a'<=grid[ni][nj]<='z':
                        q.append((ni, nj, keys + grid[ni][nj], steps + 1))
                        seen.add((ni, nj, keys))
        return -1