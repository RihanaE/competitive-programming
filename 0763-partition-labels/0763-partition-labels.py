class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for i, n in enumerate(s):
            d[n]=i
            
        l=0
        end=0
        size=0
        res=[]
        
        while l < len(s):
            
            if end < d[s[l]]:
                end=d[s[l]]
                size +=1
                
            elif end >= d[s[l]]:
                size +=1
                
            if end == l:
                res.append(size)
                size=0
                
            l +=1
            
        return res