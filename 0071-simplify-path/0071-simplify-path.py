class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pointer = 0
        temp = []
        
        while pointer < len(path):
            if path[pointer] == "/":
                if temp == [".", "."]:
                    if stack:
                        stack.pop()
                    
                    temp = []
                    
                elif temp == ["."]:
                    temp = []
                    
                else:
                    if temp != []:
                        stack.append("".join(temp))
                        
                    temp = []
                
                pointer += 1
                
            else:
                temp.append(path[pointer])
                pointer += 1
                
        if temp == [".", "."]:
            if stack:
                stack.pop()
                    
            temp = []
                    
        elif temp == ["."]:
            temp = []
                    
        if temp:
            stack.append("".join(temp))
            
        return "/" + "/".join(stack)