class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            answer=n
            
        else:
            answer=self.fib(n - 1) + self.fib(n - 2)
            
        return answer
        