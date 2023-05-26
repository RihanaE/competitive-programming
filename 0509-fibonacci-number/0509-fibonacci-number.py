class Solution:
    def fib(self, n: int) -> int:
        store = defaultdict(int)
        
        
        def compute(n):
            if n == 1:
                return 1
            
            elif store[n] != 0:
                return store[n]
            
            elif n == 0:
                return 0
            
            store[n] = compute(n - 1) + compute(n - 2)
            return store[n]
        
        return compute(n)