class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l ,r=0 , 0
        res=0
        if len(s) == 1:
            return 1
        
        while r < len(s):
            if r < len(s) and s[r] in s[l:r]:
                res = max(res, r - l)
                l +=1
                r =l + 1

            else:
                r +=1
                #res=max(res, r - 1)

        res=max(res, r - l)
        return res