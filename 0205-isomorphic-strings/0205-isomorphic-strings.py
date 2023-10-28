class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        diction = defaultdict(str)
        
        if len(s) != len(t):
            return False
        
        for i in range(len(t)):
            if t[i] not in diction and s[i] not in diction.values():
                diction[t[i]] = s[i]
                
            else:
                if (diction[t[i]] != s[i]) or (t[i] not in diction and s[i] in diction.values()):
                    return False
                
        return True