class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path= path + "/"
        res="/"
        s=""
        i=0
        
        while i < len(path):
            
            if path[i] == "/":
                if s == ".." and stack:
                    stack.pop()
                    s=""
                    
                elif s == "..":
                    s= ""
                    
                    
                elif s == ".":
                    s=""
                
                elif s != "":
                    stack.append(s)
                    s=""
                

            else:
                s +=path[i]
                
                
            i +=1
                
        res += "/".join(stack)
        return res