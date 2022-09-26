class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if int(n) == 3 and n % 3 == 0 or n == 1:
            return True
        
        else:
            if n % 3 != 0 or n == 0:
                return False
            
            return(self.isPowerOfThree(n/3))
        