class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str(self.helper(n, k))
        
        
    def helper (self, n , k):
        if n == 1:
            return 0
        
        else:
            if 2 * (2 ** (n - 2)) - 1 >= k:
                return self.helper(n - 1, k)
            
            elif 2 * (2 ** (n - 2)) == k:
                return 1
            
            else:
                return 1 - self.helper(n - 1, k - (2 * (k - ( 2 ** (n - 1)))))