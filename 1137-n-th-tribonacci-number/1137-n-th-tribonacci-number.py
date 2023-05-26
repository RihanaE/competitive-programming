class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        
        def compute(n):
            if n == 0:
                return 0
            
            elif n == 1:
                return 1
            
            elif n == 2:
                return 1
            
            elif memo[n]:
                return memo[n]
            
            memo[n] = compute(n - 3) + compute(n - 2) + compute(n - 1)
            return memo[n]
        
        return compute(n)