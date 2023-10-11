class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        pointer = 0
        
        for src, dst in edges:
            graph[src].append([dst, succProb[pointer]])
            graph[dst].append([src, succProb[pointer]])
            pointer += 1
            
        queue = [[-1, start_node]]
        visited = set()
        
        while queue:
            prob, node = heappop(queue)
            visited.add(node)
            
            if node == end_node:
                print(node)
                return abs(prob)
            
            for child, weight in graph[node]:
                if child not in visited:
                    heappush(queue, [weight * prob, child])
                    
        return 0