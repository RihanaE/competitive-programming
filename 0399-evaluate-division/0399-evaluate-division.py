class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        collection = set()
        
        for _ in range(len(values)):
            collection.add(equations[_][0])
            collection.add(equations[_][1])
            graph[equations[_][0]].append([equations[_][1], values[_]])
            graph[equations[_][1]].append([equations[_][0], 1 / values[_]])
            
        res = []
        
        
        for nume, deno in queries:
            if nume not in collection or deno not in collection:
                res.append(-1)
                continue
                
            stack = [[1, nume]]
            visited = set()
            flag = False
            
            while stack:                
                value, node = stack.pop()
                visited.add(node)
                if node == deno:
                    res.append(value)
                    flag = True
                    break
                    
                for child, weight in graph[node]:
                    if child not in visited:
                        stack.append([value * weight, child])
                        
            if not flag:
                res.append(-1)
                        
        return res