class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output=[]
        count=0
        length=len(spaces)
        
        for i in range(len(s)):
            if count < length and i == spaces[count]:
                output.append(" ")
                count +=1
                
            output.append(s[i])
            
        return "".join(output)