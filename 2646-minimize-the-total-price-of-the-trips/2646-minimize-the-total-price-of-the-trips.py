class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        counter = [0] * n
        graph = defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        def dfs(node, dest):
            if node == dest:
                counter[node] += 1
                return True
            
            visited.add(node)
            for child in graph[node]:
                if child not in visited and dfs(child, dest):
                    counter[node] += 1
                    return True
                
            return False
        
     
        
        for src, dest in trips:
            visited = set()
            dfs(src, dest)
            
        
        
        @cache
        def dp(node, isPicked, parent):
            if isPicked:
                cost = counter[node] * (price[node] // 2)
                
            else:
                cost = counter[node] * price[node]
            
            
            for child in graph[node]:
                if child != parent:
                    if isPicked:
                        nw_cost = dp(child, False, node)
                        
                    else:
                        nw_cost = min(dp(child, False, node), dp(child, True, node))
                        
                    cost += nw_cost
                    
            return cost
        
        res = float("inf")
        for i in range(n):
            res = min(res, dp(i, True, None), dp(i, False, None))
            
        return res