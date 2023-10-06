class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = []
        
        for i in s:
            if not stack:
                stack.append([i, 1])
                
            else:
                if stack[-1][0] == i:
                    count = stack[-1][1] + 1
                    stack.append([i, count])
                    
                else:
                    stack.append([i, 1])
                    
            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()
                    
        for letter, count in stack:
            res.append(letter)
            
        ans = "".join(res)
        return ans