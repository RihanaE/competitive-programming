class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def getPrimes():
            lst = [True] * (right + 1)
            lst[0] = lst[1] = False
          
            mul = 2
            for i in range(2, right + 1):
                if mul * i <= right and lst[mul * i ] == False:
                    pass

                while mul * i <= right: 
                   
                    lst[mul * i ] = False
                    mul += 1

                if i * i > right:
                    break

                mul = 2
            res = []
            for i in range(left, right + 1):
                if lst[i] == True:
                    res.append(i)
            return res

        primes = getPrimes()
        diff = right - left + 1
        res = [-1, -1]
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < diff:
                diff = primes[i] - primes[i - 1] 
                res = [primes[i - 1], primes[i]]

        return res