class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        l, r=0, 1
        
        while r < len(prices):
            if r < len(prices) and prices[l] < prices[r]:
                res=max(res, prices[r] - prices[l])
                
            elif prices[l] > prices[r]:
                l=r
            
                
            r +=1
            
                
        return res