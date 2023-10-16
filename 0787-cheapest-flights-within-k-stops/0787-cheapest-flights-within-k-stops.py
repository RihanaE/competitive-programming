class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for to, from_, cost in flights:
            graph[to].append([from_, cost])
                
        arr = [float("inf")] * n
        arr[src] = 0
        temp = arr[:]
        
        for _ in range(k + 1):
            queue = deque([[None, src]])
            visited = set()
            
            while queue:
                parent, node = queue.popleft()
                
                if node in visited:
                    continue
                    
                visited.add(node)
                
                for child, weight in graph[node]:
                    if temp[child] > arr[node] + weight:
                        temp[child] = arr[node] + weight
                    
                    if parent != child:
                        queue.append([node, child])
                    
            arr = temp[:]
            
        if arr[dst] != float("inf"):
            return arr[dst]
        
        return -1
        
        