class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        res=0
        
        for i in operations:
            if i == "C":
                stack.pop()
                
            elif i == "D":
                stack.append(stack[-1] * 2)
                
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
                
            else:
                stack.append(int(i))
                
        for i in stack:
            res +=i
            
            
        return res