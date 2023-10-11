class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        pointer1 = 0
        pointer2 = 0
        res = 0
        
        while pointer1 < len(s) and pointer2 < len(g):
            if s[pointer1] >= g[pointer2]:
                res += 1
                pointer1 += 1
                pointer2 += 1
                
            else:
                pointer1 += 1
                
        return res