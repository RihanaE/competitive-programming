class Solution:
    def isPalindrome(self, s: str) -> bool:
        store=""
        
        for i in s:
            if i.isalnum():
                store +=i.lower()
                
        return store == store[::-1]