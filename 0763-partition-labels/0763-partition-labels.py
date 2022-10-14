class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        stack=[]
        
        for i in range(len(s)):
            d[s[i]]=i
            
        i=0
        size=0
        end=0
        
        while i < len(s):
            size +=1
            
            if d[s[i]] > end:
                end = d[s[i]]
                
            if end == i:
                stack.append(size)
                size =0
                
            i +=1
            
        return stack