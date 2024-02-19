class Solution:
    def reverseBits(self, n: int) -> int:
        ls = []
        
        while n != 0:
            ls.append(n % 2)
            n = n // 2
            
        ls = ls[::-1]
        res = 0
        
        if len(ls) < 32:
            ls = ([0] * (32 - len(ls))) + ls
            
        for i in range(len(ls)):
            res += ((2) ** i) * ls[i]
            
        return res