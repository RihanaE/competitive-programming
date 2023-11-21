class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS = 0
        pointerT = 0
        
        if len(s) > len(t):
            return False
        
        while pointerS < len(s) and pointerT < len(t):
            if s[pointerS] == t[pointerT]:
                pointerT += 1
                pointerS += 1
                
            else:
                pointerT += 1
                
        if pointerS < len(s):
            return False
        return True