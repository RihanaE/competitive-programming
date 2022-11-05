class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)
        
        l , r=0, 1
        check=1
        res=count=1
        
        while r < len(s):
            if s[check] in s[l: r] :
                res=max(res, count)
                l +=1
                r =l + 1
                check= r
                count=1
                
            elif s[check] not in s[l : r]:
                r +=1
                count +=1
                check +=1
          
        res=max(res, count)
        return res