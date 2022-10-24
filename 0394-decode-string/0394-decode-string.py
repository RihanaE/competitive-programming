class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        no="0123456789"
        l=0
        res=""
        num=""
        while l < len(s):
            if s[l] != "]":
                stack.append(s[l])
                l +=1
                
            elif s[l] == "]":
                while stack[-1] != "[":
                    res +=stack.pop()
                    
                stack.pop()
                res=res[::-1]
                
                while stack and stack[-1] in no:
                    num +=stack.pop()
                    
                num=num[::-1]
                out=int(num) * res
                
                for i in out:
                    stack.append(i)
                    
                res=""
                num=""
                l +=1
                
        return "".join(stack)