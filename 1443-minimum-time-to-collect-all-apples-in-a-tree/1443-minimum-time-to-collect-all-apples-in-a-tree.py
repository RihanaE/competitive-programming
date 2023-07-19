class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set([0])
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
            
        
        def dfs(node, node_pr):
            res = 0
            
            for i in graph[node]:
                if i == node_pr:
                    continue
                    
                resT = dfs(i, node)
                
                if resT or hasApple[i]:
                    res = res + resT + 2
                    
            return res
        
        return dfs(0, -1)
                    
                    

            
        return dfs(0)