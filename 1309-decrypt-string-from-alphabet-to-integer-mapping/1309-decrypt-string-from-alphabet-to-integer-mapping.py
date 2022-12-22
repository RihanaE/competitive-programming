class Solution:
    def freqAlphabets(self, s: str) -> str:
        dictionary={}
        for i in range(1,27):
            if i <= 9:
                dictionary[f"{i}"]=chr(96 + i)
                
            else:
                dictionary[f"{i}#"]=chr(96 + i)
                
        right= len(s) - 1
        output =""
        
        while right >= 0:
            if s[right] == "#":
                output += dictionary[s[right - 2:right + 1]]
                right -= 3
                
            else:
                output +=dictionary[s[right]]
                right -=1
                
        return output[::-1]