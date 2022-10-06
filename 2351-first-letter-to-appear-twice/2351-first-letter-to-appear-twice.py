class Solution:
    def repeatedCharacter(self, s: str) -> str:
        output=[]
        
        for i in s:
            if output == []:
                output.append(i)
                
            elif output != [] and i not in output:
                output.append(i)
                
            else:
                return i
                
            
        