class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        elif n == float(1):
            return True
        
        else:
            return self.isPowerOfFour(n / 4)