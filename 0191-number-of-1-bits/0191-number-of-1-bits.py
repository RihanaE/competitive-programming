class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n != 0:
            if n % 2 != 0:
                res += 1
                
            n = n // 2
            
        return res