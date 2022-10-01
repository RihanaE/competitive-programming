class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=["*", "/" , "-" , "+"]
        stack=[]
        
        for i in tokens:
            if i not in l:
                stack.append(int(i))
                
            if i == "*":
                res=stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
                
            elif i == "-":
                res=stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
                
            elif i == "+":
                res=stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
                
            elif i == "/":
                if stack[-2] * stack[-1] >= 0 or stack[-2] % stack[-1] == 0:
                    res=stack[-2] // stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                    
                else:
                    res=stack[-2] // stack[-1] + 1
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                
        return stack[-1]
        