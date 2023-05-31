class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        elif n == 1:
            return 1

        else:
            res = [0, 1]
            memo = {0 : 0, 1 : 1}

            def compute(n):
                if n in memo:
                    return memo[n]

                elif n % 2 == 0:
                    memo[n] = compute(n // 2)
                    return memo[n]

                else:
                    
                    memo[n] = compute(n // 2) + compute((n // 2) + 1)
                    return memo[n]

            for i in range(2, n + 1):
                res.append(compute(i))
            
    
            return max(res)