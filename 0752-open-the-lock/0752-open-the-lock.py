class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if "0000" in deadends:
            return -1
        
        graph = defaultdict(list)
        
        for i in range(10):
            if i == 0:
                graph[i].append(1)
                graph[i].append(9)
                
            elif i == 9:
                graph[i].append(0)
                graph[i].append(8)
                
            else:
                graph[i].append(i - 1)
                graph[i].append(i + 1)
            
        
        queue = deque([[[0, 0, 0, 0], 0]])    
        visited = set([tuple([0,0,0,0])])
        
        def bfs():
            
            while queue:
              
                curr, res = queue.popleft()
                str_ =  str(curr[0]) + str(curr[1]) + str(curr[2]) + str(curr[3])
                
                if str_ == target:
                    return res
                
                for i in range(len(curr)):
                    temp = curr[i]
                    
                    curr[i] = graph[temp][0]
                    
                    if tuple(curr) not in visited and str_ not in deadends:
                        
                        queue.append([curr[:], res + 1])
                        visited.add(tuple(curr))
                        
                    
                    curr[i] = graph[temp][1]
                    
                    if tuple(curr) not in visited and str_ not in deadends:
                        
                        queue.append([curr[:], res + 1])
                        visited.add(tuple(curr))
                        
                    curr[i] = temp
            
            return -1
        
        return bfs()
    
                    