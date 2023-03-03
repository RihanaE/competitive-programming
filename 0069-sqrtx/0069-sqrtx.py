class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        mid = 0
        
        while l <= r :
            mid = (l + (r - l)//2)
            
            temp = mid * mid
            
            if temp == x:
                return mid
            
            elif temp < x:
                l = mid + 1
                
            else:
                r = mid - 1
                
        return r