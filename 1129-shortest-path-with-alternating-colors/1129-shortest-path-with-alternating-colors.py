class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * (n)
        res[0] = 0
        graph = defaultdict(list)
        
        for src, dest in redEdges:
            graph[src].append([dest, "r"])
            
        for src, dest in blueEdges:
            graph[src].append([dest, "b"])
            
        queue = deque([[0, None, 0]])
        visited = set([(0, None)])
        
        while queue:
            node, color, dis = queue.popleft()
            
            for neigh, cl in graph[node]:
                if (neigh, cl) not in visited and cl != color:
                    if res[neigh] == -1:
                        res[neigh] = dis + 1
                        
                    visited.add((neigh, cl))
                    queue.append([neigh, cl, dis + 1])
                    
        return res