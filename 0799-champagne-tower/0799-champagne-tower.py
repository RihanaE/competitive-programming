class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []
        
        for i in range(1, 101):
            dp.append([0] * i)
            
        dp [0][0] = poured
        
        for i in range(99):
            for j in range(i+1):
                add = max((dp[i][j] - 1) /2, 0)
                dp[i+1][j] += add
                dp[i+1][j+1] += add
                dp[i][j] = min(1, dp[i][j])
                
        return dp[query_row][query_glass]