class Solution:
    def calculate(self, s: str) -> int:
        l = 0
        res = 0
        curr, pre=0 , 0
        sign="+"
        
        

        while l < len(s):
            char=s[l]
            
            if char.isdigit():
                while l < len(s) and s[l].isdigit():
                    curr=curr*10 + int(s[l])
                    
                    l+=1
                    
                l -=1
                
                if sign == "+":
                    res +=curr
                    pre=curr
                    
                elif sign == "-":
                    res -=curr
                    pre= -curr
                    
                elif sign =="*":
                    res -=pre
                    
                    res += pre * curr
                    pre=pre * curr
                    
                elif sign == "/":
                    res -=pre
                    res += int(pre / curr)
                    pre=int(pre / curr)
                 
                curr= 0
            elif char != " ":
                sign = char
                
            l +=1
            
        return res