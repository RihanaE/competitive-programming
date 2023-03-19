class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        store = {}
        
        for i in range(len(edges)):
            if edges[i][0] in store:
                store[edges[i][0]].append(edges[i][1])
                
            else:
                store[edges[i][0]] = [edges[i][1]]
                
            if edges[i][1] in store:
                store[edges[i][1]].append(edges[i][0])
                
            else:
                store[edges[i][1]] = [edges[i][0]]
                
        return self.helper(store, source, destination)
        
    def helper(self, store, src, dest):
        stack = [src]
        
        while stack:
            
            value = stack.pop()
            if value == dest:
                return True
            
           
            temp = store[value]
            while temp:
                stack.append(temp.pop())
                
        return False