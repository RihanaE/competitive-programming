class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        weight = defaultdict(int)
        store = defaultdict(list)
        visited = set()
        
        for pre, next_ in prerequisites:
            store[next_].append(pre)
            weight[pre] += 1
            
        queue = deque()
        
        
        for i in range(numCourses):
            
            if weight[i] == 0:
                queue.append(i)
                visited.add(i)
                
                
        while queue:
            node = queue.popleft()
            
            for neigh in store[node]:
                if neigh not in visited:
                    weight[neigh] -= 1
                    
                    if weight[neigh] == 0:
                        queue.append(neigh)
                        visited.add(neigh)
                        
      
        return len(visited) == numCourses