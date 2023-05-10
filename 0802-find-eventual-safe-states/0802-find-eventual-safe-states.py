class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        weight = defaultdict(int)
        res = []
        queue = deque()
        visited = set()
        
        for node in range(len(graph)):
            for val in graph[node]:
                
                store[val].append(node)
                
                weight[node] += 1
            
        for i in range(len(graph)):
            if weight[i] == 0:
                queue.append(i)
                res.append(i)
                visited.add(i)
                
       
        
        while queue:
            node = queue.popleft()
            
            for neigh in store[node]:
                
                weight[neigh] -= 1
                    
                if weight[neigh] == 0:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
                        res.append(neigh)
                        
        return sorted(res)