class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        store = [True for i in range( right + 1)]
        
        store[0] = False
        store[1] = False
        
        
        for i in range(right + 1):
            
            if store[i]:
                for j in range(i * i, right + 1, i):
                    store[j] = False
            
       
        candidate = []
        res = float('inf')
        ans = None
        for i in range(left, right + 1):
            if store[i]:
                candidate.append(i)
                
       
        for i in range(1, len(candidate)):
            if candidate[i] - candidate[i - 1] < res:
                res = candidate[i] - candidate[i - 1]
                ans = [candidate[i- 1], candidate[i]]
                
                
        if not ans:
            return [-1, -1]
                
                
        return ans