class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        amount = n
        for i in range(1, n + 1):
            if amount - i >= 0:
                res += 1
                amount -= i
                
            else:
                break
                
        return res