class Solution:
    def countArrangement(self, n: int) -> int:
        seen = [0] * n
        count = 0
        
        def helper(num):
            nonlocal count
            nonlocal seen 
            
            
            if num >= n:
                count += 1
            
            for i in range(1, n + 1):
                if seen[i - 1] == 0 and (i % (num + 1) == 0 or (num + 1) % i == 0):
                    seen[i - 1] = 1
                    helper(num + 1)
                    seen[i - 1] = 0
                    
        helper(0)
        return count