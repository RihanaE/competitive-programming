class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        diction = defaultdict(int)
        pointer = 0
        
        while pointer < len(s):
            
            if not stack:
                stack.append([s[pointer], 1])
            
            else:
                if stack[-1][0] == s[pointer]:
                    stack.append([s[pointer], stack[-1][1] + 1])
                    
                else:
                    stack.append([s[pointer], 1])
                    
            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()
                    
            pointer += 1
            
            
        res = ""
        
        for val, cnt in stack:
            res += val
            
        return res