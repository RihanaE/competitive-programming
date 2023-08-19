class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn = defaultdict(int)
        tn = defaultdict(int)
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sn[s[i]] += 1
            tn[t[i]] += 1
            
        for j in s:
            if j not in tn or sn[j] != tn[j]:
                return False
            
        for j in t:
            if j not in sn or sn[j] != tn[j]:
                return False
            
        return True