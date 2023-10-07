class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for src, dest, weight in times:
            graph[src].append([dest, weight])
            
        queue = [[0, k, None]]
        visited = set()
        
        while queue:
            distance, node, parent = heappop(queue)
            visited.add(node)
            res = distance
            if len(visited) == n:
                return res
            
            for child, weight in graph[node]:
                if child != parent and child not in visited:
                    heappush(queue, [distance + weight, child, node])
                    
        return -1