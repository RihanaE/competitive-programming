class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = 0
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        for i in graph:
            if res <= len(graph[i]):
                res = len(graph[i])
                ans = i
                
        return ans