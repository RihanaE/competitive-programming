class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {val: ind for ind, val in enumerate(s)}
        stack = []
        
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                
            elif s[i] not in stack and stack[-1] > s[i]:
                while stack and stack[-1] > s[i] and dic[stack[-1]] > i:
                    stack.pop()
                    
                stack.append(s[i])
                
            elif s[i] not in stack:
                stack.append(s[i])
                
        return "".join(stack)