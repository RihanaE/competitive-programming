class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4300:
            return 1
        
        memo = {}
        
        def helper(A, B):
            if (A, B) in memo:
                return memo[(A, B)]
            
            if A <= 0 and B <= 0:
                return 0.5
            
            if A <= 0:
                return 1
            
            if B <= 0:
                return 0
            
            prob = 0.25 * (helper(A - 100, B) + helper(A - 75, B - 25) + helper(A - 50, B - 50) + helper(A - 25, B - 75))
            
            memo[(A, B)] = prob
            return prob
            
        return helper(n, n)