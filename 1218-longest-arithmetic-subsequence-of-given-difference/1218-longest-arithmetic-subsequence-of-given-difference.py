class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        mx = 0
        for i in arr:
            if i - difference in dp:
                dp[i] = 1 + dp[i - difference]
                mx = max(mx, dp[i])
                
            else:
                dp[i] = 1
                mx = max(mx, dp[i])
                
                
        return mx