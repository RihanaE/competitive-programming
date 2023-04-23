class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        store = {i:None for i in range(1, n + 1)}
        
        def dfs(node, pre):
            if not store[node]:
                store[node] = pre
            
            else:
                return store[node] == pre
        
            for i in graph[node]:
                if pre == "r":
                    if not dfs(i, "b"):
                        return False
                    
                else:
                    if not dfs(i,"r"):
                        return False
                    
            return True
                    
        for i in range(1, n + 1):
            if not store[i] and not dfs(i, "b"):
                return False
            
        return True