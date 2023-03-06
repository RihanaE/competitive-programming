class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:

            if n < 0:
                n = n * -1
                return 1/x * self.myPow(1 / x, n - 1)
            elif n % 2 !=0:
                return x * self.myPow(x, n - 1)

            elif n % 2 == 0:
                temp=self.myPow(x,n//2)

                return temp * temp