class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        edge = defaultdict(int)
        visited = set()
        res = 0


        for src, dest in edges:
            graph[src].append(dest)
            edge[src] += 1
            edge[dest] += 1
            graph[dest].append(src)

        def dfs(node, res):
            if node in visited:
                return 

            visited.add(node)
            res.append(node)
            for child in graph[node]:
                dfs(child, res)

            return res

        for i in range(n):
            if i not in visited:
                component = dfs(i, [])
                flag = True

                for c in component:
                    if edge[c] != len(component) - 1:
                        flag = False
                        break
                    
                if flag:
                    res += 1

        return res
