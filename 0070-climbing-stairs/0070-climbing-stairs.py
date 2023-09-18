class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1:1, 2 : 2}
        
        def backtrack(n):
            if n in dp:
                return dp[n]
            
            dp[n] = backtrack(n - 1) + backtrack(n - 2)
            return dp[n]
        
        return backtrack(n)