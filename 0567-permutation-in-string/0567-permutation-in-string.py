class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1={}
        d2={}
        for i in s1:
            if i not in d1:
                d1[i]=1
                
            else:
                d1[i] +=1
                
        j=len(s1)
        l=r=0
        
        while r < len(s2):
            if r - l + 1 <= j:
                if s2[r] not in d2:
                    d2[s2[r]]=1
                    
                else:
                    d2[s2[r]] +=1
                    
                r +=1
                
            else:
                if d1 == d2:
                    return True
                else:
                    d2[s2[l]] -=1
                    if d2[s2[l]] == 0:
                        del(d2[s2[l]])
                    
                    l +=1
                    
        if d1 == d2:
            return True
        return False