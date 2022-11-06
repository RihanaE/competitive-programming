class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        count=0
        l=0
        
        while l < len(s):
            if s[l].isalnum():
                count +=1
                
            else:
                count=0
                
            l +=1
            
        return count