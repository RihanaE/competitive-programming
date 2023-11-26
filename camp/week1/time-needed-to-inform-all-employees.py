class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        queue = deque()        
        
        for ind, val in enumerate(manager):
            graph[val].append(ind)
            
                
                
        res = 0
        visit = set()
        queue = deque({(headID, 0)})
        
        while queue:
            idx, t = queue.popleft()
            # visit.add((idx, t))
            
            res = max(res, t)
            
            for child in graph[idx]:
                # if (child, t + informTime[child]) not in visit:
                queue.append([child, t + informTime[idx]])
                
        return res