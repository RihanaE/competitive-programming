class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = []
        
        for i in range (n + 1):
            dp.append([0, 0])
        
    

        for inx in range(n - 1, -1, -1):
            for buy in range(2):

                if buy == 1:
                    profit = max(dp[inx + 1][0] - prices[inx], dp[inx + 1][1])

                else:
                    profit = max(prices[inx] + dp[inx + 1][1] - fee, dp[inx + 1][0])

                dp[inx][buy] = profit
  
        return dp[0][1]