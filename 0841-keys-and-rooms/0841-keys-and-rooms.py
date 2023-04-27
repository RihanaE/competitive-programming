class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key = set()
        graph = defaultdict(list)
        
        for i in range(len(rooms)):
            graph[i] = rooms[i]
            
        
        queue = deque([0])
        
        while queue:
            value = queue.popleft()
            key.add(value)
            
            for i in graph[value]:
                if i not in key:
                    queue.append(i)
                    
        return len(rooms) == len(key)