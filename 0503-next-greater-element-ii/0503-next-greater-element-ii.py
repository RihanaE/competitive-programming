class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = []
        stack1 = []
        
        for ind, val in enumerate(nums):
            if not stack:
                stack.append([val, ind])
                
            elif val > stack[-1][0]:
                while stack and val > stack[-1][0]:
                    res[stack[-1][1]] = val
                    stack.pop()
                stack.append([val, ind])
                
            else:
                stack.append([val, ind])
            
            stack1.append([val, ind])
                
        
        left = 0
        right = len(stack) - 1
        
        while right > 0 and left < len(stack1):
            if stack[right][0] < stack1[left][0]:
                res[stack[right][1]] = stack1[left][0]
                stack1.append(stack.pop())
                right -= 1
                
            else:
                left += 1
                
        print(stack)
#         for i in range(len(stack) - 1, -1, -1):
#             if not stack1:
#                 stack1.append(stack[i])
                
#             elif stack1[-1][0] < stack[i][0]:
#                 while stack1 and stack1[-1][0] < stack[i][0]:
#                     res[stack1[-1][1]] = stack[i][0]
#                     stack1.pop()
                    
#                 stack1.append(stack[i])
                
#             else:
#                 stack1.append(stack[i])
                
        
        for i in range(len(stack)):
            res[stack[i][1]] = -1
            
        return res