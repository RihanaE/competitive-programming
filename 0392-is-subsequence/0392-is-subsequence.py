class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        leftPointer = 0
        
        if len(s) == 0:
            return True
        
        elif len(s) > len(t):
            return False
        
        for i in s:
            if leftPointer >= len(t):
                return False
            
            while leftPointer < len(t):
                if i == t[leftPointer]:
                    leftPointer += 1
                    flag = True
                    break
                    
                else:
                    flag = False
                    leftPointer += 1
                    
            if not flag:
                return False
            
        return True