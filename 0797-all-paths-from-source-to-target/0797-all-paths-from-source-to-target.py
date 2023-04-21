class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        n = len(graph) - 1
        res = []
        visited = set()
        
        for i in range(len(graph)):
            for j in graph[i]:
                g[i].append(j)
                
                
        def dfs(root, path):
            nonlocal res
            
            
            
            if root != 0 and not root:
                return
            
            
            if root == n:
                res.append(path[:])
                
                return
                
            
            for i in g[root]:
                dfs(i, path + [i])
                    
        dfs(0, [0])
        return res