class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        pointer = len(s) - 1
        for i in range(len(s)):
            num += (2 ** i) * int(s[pointer]) 
            pointer -= 1
            
        steps = 0
        while num != 1:
            steps += 1
            if num % 2 == 0:
                num = num // 2
                
            else:
                num += 1
                
        return steps