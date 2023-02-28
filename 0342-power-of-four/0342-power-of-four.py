class Solution:
    def isPowerOfFour(self, n, temp = 1):
        
        
        if temp == n:
            return True
        elif temp > n:
            return False
        
        else:
            return self.isPowerOfFour(n, temp * 4)