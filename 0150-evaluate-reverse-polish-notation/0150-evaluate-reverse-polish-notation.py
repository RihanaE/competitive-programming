class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = set("+-*/")
        stack = []
        
        for i in tokens:
            if i in operation:
                temp = int(stack.pop())
                temp1 = int(stack.pop())
                
                if i == "*":
                    stack.append(temp1 * temp)
                    
                elif i =="-":
                    stack.append(temp1 - temp)
                    
                elif i == "+":
                    stack.append(temp1 + temp)
                    
                elif i == "/":
                    stack.append(int(temp1 / temp))
                    
            else:
                stack.append(i)
                
        return int(stack[0])