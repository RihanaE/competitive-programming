class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = defaultdict(list)
        weight = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        visited = set()
        
        for i in edges:
            graph[i[0]].append(i[1])
            weight[i[1]] += 1
            
        for i in range(n):
            if weight[i] == 0:
                queue.append(i)
                visited.add(i)
                ans[i] = []
                
        while queue:
            node = queue.popleft()
            
            for neigh in graph[node]:
                if neigh not in visited:
                    weight[neigh] -= 1

                    if node not in ans[neigh]:
                        ans[neigh].append(node)
                        ans[neigh].extend(ans[node])

                    if weight[neigh] == 0:
                        visited.add(neigh)
                        queue.append(neigh)
                        temp = set(ans[neigh])
                        ans[neigh] = list(temp)
                        ans[neigh].sort()
                        
                        
        res = []
        
        for i in range(n):
            res.append(ans[i])
            
        return res