class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        total = set()
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            total.add(src)
            total.add(dest)
            
        ans = 0
        res = None
        for i in graph:
            if len(graph[i]) > ans:
                res = i
                ans = len(graph[i])
                
        return res