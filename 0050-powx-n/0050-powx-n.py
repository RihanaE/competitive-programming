class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        elif n < 0:
            return 1.0 / self.myPow(x, -n)

        if n % 2 != 0:
            return x * self.myPow(x, n - 1)

        else:
            temp = self.myPow(x, n // 2)
            return temp * temp
