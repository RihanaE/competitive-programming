class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        store = []
        
        for i in matrix:
            store.extend(i)
            
        heapify(store)
        
        for i in range(k):
            value = heappop(store)
            
        return value