class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        store, height = self.initialize(n)
        
        def rep(node):
            while node != store[node]:
                node = store[node]
                
            return node
        
        def union(x, y):
            rep_x = rep(x)
            rep_y = rep(y)
            
            if height[rep_x] > height[rep_y]:
                store[rep_y] = rep_x
                height[rep_y] = max(height[rep_x] + 1, height[rep_y])
                
            else:
                store[rep_x] = rep_y
                height[rep_x] = max(height[rep_y] + 1, height[rep_x])
                
                
        def connected(node1, node2):
            return rep(node1) == rep(node2)
        
        for node1 , node2 in edges:
            union(node1, node2)
            
        return connected(source, destination)
                
                
        
        
    def initialize(self, n):
        store = defaultdict(int)
        height = defaultdict(int)
        
        for i in range(n):
            store[i] = i
            height[i] = 1
            
        return store, height
            
        