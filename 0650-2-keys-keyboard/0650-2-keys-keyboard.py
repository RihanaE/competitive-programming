class Solution:
    def minSteps(self, n: int) -> int:
        word = 1
        clip = 0
        step = 0
        
        while word != n:
            if n % word == 0:
                clip = word
                step += 1
                
                word += clip
                step += 1
                
            else:
                word += clip
                step += 1
                
        return step