class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack1 = []
        stack = []
        level = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                stack1.append(s[i])

                if len(stack) < len(stack1):
                    stack.append(0)
                    
                level += 1
                    
            else:
                level -= 1
                if level + 1 == len(stack):
                    stack[level] += 1
                    stack1.pop()
                
                else:
                    temp = stack.pop() * 2
                    stack[-1] += temp
                    stack1.pop()
                    
        return stack[0]