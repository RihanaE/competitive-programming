class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        nw_val = 2 * n 
        
        for i in range(nw_val, 0, -1):
            res *= i
            
        ans = (( res ) // (2 ** n)) % ((10 ** 9) + 7)
        
        return ans