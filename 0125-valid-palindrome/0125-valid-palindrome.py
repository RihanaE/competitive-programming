class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s) - 1
        s=s.lower()
        while l <= r:
            if 48 <= ord(s[l]) <=57 or 97 <= ord(s[l]) <= 122:
                if 48 <= ord(s[r]) <=57 or 97 <= ord(s[r]) <= 122:
                    if s[l] != s[r]:
                        return False
                    
                    l +=1
                    r -=1
                    
                else:
                    r -=1
                    
            else:
                l +=1
                
        return True