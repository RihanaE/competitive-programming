class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        mn = 0 
        
        if sum(piles) // h == 0:
            mn = 1
            
        else:
            mn = sum(piles) // h
            
        l = mn 
        r = max(piles)
        stack = 0
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if self.helper(piles, mid, h):
                stack = mid
                r = mid - 1
                
            else:
                l = mid + 1
            
        
        return stack
        
    def helper(self, piles, n, h):
        res = 0 
        for i in piles:
            
            if i % n == 0:
                res = res + (i //n)
                
            else:
                res = res +((i // n) + 1)
            
        return res <= h