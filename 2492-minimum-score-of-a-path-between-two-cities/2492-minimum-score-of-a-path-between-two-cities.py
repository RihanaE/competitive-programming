class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        store, rank = self.initialize(n)
        
        def rep(node):
            temp = node
            while node != store[node]:
                node = store[node]
                
            while temp != node:
                temp, store[temp] = store[temp], node
                
            return node
#             if node != store[node]:
#                 store[node] = rep(store[node])

#             return node

        def union(node1, node2, weight):
            rep_node1 = rep(node1)
            rep_node2 = rep(node2)
            
            
            rank[rep_node2] = min(rank[rep_node1], rank[rep_node2], weight)
            store[rep_node1] = rep_node2
            
        for _to, _from, weight in roads:
            union(_to, _from, weight)
            
     
        
        return rank[rep(1)]
        
        
        
        
        
    def initialize(self, n):
        store = defaultdict(int)
        rank = {i : float('inf') for i in range(1, n + 1) }
        
        for i in range(1, n + 1):
            store[i] = i
            
        return store, rank