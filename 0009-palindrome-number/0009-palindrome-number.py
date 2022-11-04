class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        check=str(x)
        check= check[::-1]
        
        return x == int(check)
            