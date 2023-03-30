class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        value = x ^ y
        count = 0
        temp = value
        
        for i in range(64):
            if temp >> i & 1 == 1:
                count += 1
                
        return count