class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r =0 , len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                sl=s[l + 1:r + 1]
                sr=s[l:r]
                return (sl == sl[::-1] or sr == sr[::-1])
            l +=1
            r -=1
            
        return True