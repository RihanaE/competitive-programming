class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res=[1] * len(prices)
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                res[i]=res[i - 1] + res[i]
                
        return sum(res)