class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op="*-+/"
        
        for i in tokens:
            if i not in op:
                stack.append(int(i))
                
            else:
                n1=stack.pop()
                n2=stack.pop()
                
                if i == "+":
                    num=n1+n2
                    
                elif i == "-":
                    num=n2 - n1
                    
                elif i == "*":
                    num=n2 * n1
                    
                elif i == "/":
                    num= int(n2 / n1)
                    
                stack.append(num)
                
        return stack[-1]