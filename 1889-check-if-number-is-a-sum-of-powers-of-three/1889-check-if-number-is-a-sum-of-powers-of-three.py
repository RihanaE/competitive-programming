class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        exp = 16

        def checker(n, exp):
            if n < 3 ** exp:
                while n < 3 ** exp:
                    exp -= 1

            else:
                exp -= 1

            return exp

        while n > 0:
            exp = checker(n, exp)
            n -= 3 ** exp

            print(n, exp)
            if exp < 0:
                return False

        return True