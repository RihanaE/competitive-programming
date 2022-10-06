class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        no=0
        
        for i,ind in count.items():
            if ind == 1:
                return s.index(i)
                
        else:
            return -1
        