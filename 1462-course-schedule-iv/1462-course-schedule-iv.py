class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        weight = defaultdict(int)
        store = defaultdict(list)
        
        def check(pre, course):
            queue = deque([pre])
            visited = set([pre])
            
            
            while queue:
                node = queue.popleft()
                if node == course:
                    return True
                
                for point in store[node]:
                    if point not in visited:
                        visited.add(point)
                        queue.append(point)
                           
                        if point == course:
                            return True
                    
                    
                        
                        
            return False
        
        ans = []
        
        for pre, next_ in prerequisites:
            store[pre].append(next_)
            weight[next_] += 1
            
        for pre, course in queries:
            if check(pre, course):
                ans.append(True)
                
            else:
                ans.append(False)
                    
        
        
        return ans