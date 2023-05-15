class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                    
                elif bombs[i][2] >= math.sqrt(((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2)):
                    graph[i].append(j)
                    
                   
                    
        res = 0
        for i in range(len(bombs)):
            visited = set([i])
            stack = [i]
            count = 1
            
            while stack:
                node = stack.pop()
                
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        stack.append(neigh)
                        count += 1
                        
            res = max(res, count)
            
        return res