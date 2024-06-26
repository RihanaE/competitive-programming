class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}
        
        
        for i in range(len(s)):
            if s[i] not in sMap and t[i] not in tMap:
                sMap[s[i]] = t[i]
                tMap[t[i]] = s[i]
                
            else:
                if s[i] not in sMap or t[i] not in tMap:
                    return False
                
                elif sMap[s[i]] != t[i] or tMap[t[i]] != s[i]:
                    return False
            
        return True