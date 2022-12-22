class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1=Counter(s)
        c2=Counter(t)
        
        for i in c2.keys():
            if i not in c1.keys():
                return i
            
            elif c2[i] != c1[i]:
                return i