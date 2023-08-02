class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        hmp = defaultdict(set)
        for bus, route in enumerate(routes): 
            for stop in route:
                hmp[stop].add(bus)
        
        q = deque()
        q.append((source, 0))
        visited = set()
        visited.add(source)
        bus_seen = set()

        while q:
            stop, count = q.popleft()
            if stop == target:
                return count
            for bus in hmp[stop]: 
                if bus not in bus_seen: 
                    bus_seen.add(bus)
                    for neighbor in routes[bus]:
                        if neighbor not in visited:
                            q.append((neighbor, count + 1))
                            visited.add(neighbor)
        return -1