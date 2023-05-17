class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        store, height = self.initialize(len(edges))
        
        
        def rep(node):
            while node != store[node]:
                node = store[node]
                
            return node
        
        def union(node1, node2, candidate):
            rep_node1 = rep(node1)
            rep_node2 = rep(node2)
            
            if rep_node1 == rep_node2:
                candidate = [node1, node2]
            
            if height[rep_node1] > height[rep_node2]:
                store[rep_node2] = rep_node1
                height[rep_node1] = max(height[rep_node2] + 1, height[rep_node1])
                
            else:
                store[rep_node1] = rep_node2
                height[rep_node2] = max(height[rep_node1] + 1, height[rep_node2])
                
            return candidate
        
        res = None
        for node1, node2 in edges:
            res = union(node1, node2, res)
            
        return res
        
    def initialize(self, n):
        store = defaultdict(int)
        height = defaultdict(int)
        
        for i in range(1, n + 1):
            store[i] = i
            height[i] = 1
            
        return store, height