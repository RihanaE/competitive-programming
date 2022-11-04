class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1 , "V":5 , "X":10, "L":50 , "C":100 , "D":500 , "M":1000 }
        l,r=len(s) - 2, len(s) - 1
        
        result = d[s[r]]
        
        while l >= 0:
            if d[s[l]] >= d[s[r]]:
                result +=d[s[l]]
                
            else:
                result -=d[s[l]]
                
            l -=1
            r -=1
            
        return result