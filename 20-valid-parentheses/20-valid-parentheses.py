class Solution:
    def isValid(self, s: str) -> bool:
        count=0
        c=[]
        so , sc=0 , 0
        co , cc=0 , 0
        cuo , cuc= 0 , 0
        
        for i in s:
            if i == "(":
                co+=1
            elif i == ")":
                cc+=1
            elif i == "[":
                so+=1
            elif i == "]":
                sc+=1
            elif i == "{":
                cuo+=1
            elif i == "}":
                cuc+=1
                
        if so != sc or co != cc or cuo != cuc:
            return False            

        for i in s:
            if c == []:
                c.append(i)

            elif i == "(" or i == "[" or i == "{":
                c.append(i)

            elif c[-1] == "(" and i == ")":
                c.pop()

            elif c[-1] == "[" and i == "]":
                c.pop()

            elif c[-1] == "{" and i == "}":
                c.pop()

            else:
                count+=1
                
            if c:
                if c[0] == "]" or c[0] == "}" or c[0] == ")":
                    count+=1

        return count == 0
