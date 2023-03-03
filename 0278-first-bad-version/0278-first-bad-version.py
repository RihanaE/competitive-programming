# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        store = 0
        
        
        while l <= r:
            mid =(l + r) // 2
            temp = isBadVersion(mid)
            
            if temp == False:
                l = mid + 1
                
            else:
                r = mid - 1
                store = mid
                
        return store