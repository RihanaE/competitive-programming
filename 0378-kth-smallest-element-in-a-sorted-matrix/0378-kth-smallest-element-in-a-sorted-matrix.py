class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        store=[]
        l=0
        r=0
        
        while l < len(matrix):
            if r < len(matrix[0]):
                store.append(matrix[l][r])
                r +=1
                
            else:
                l +=1
                r=0
        store.sort()
        
        for i in range(k):
            if i == k - 1:
                return store[i]
        