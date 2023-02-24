class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)
        
        for ind, val in enumerate(temp):
            
            if not stack or stack[-1][0] >= val:
                stack.append([val, ind])
                
                
            elif stack[-1][0] < val:
                while stack and stack[-1][0] < val:
                    
                    res[stack[-1][1]] = ind - stack[-1][1]
                    stack.pop()
                    
                stack.append([val,ind])
                
                
        
        return res