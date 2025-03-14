class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sm = sum(candies)
        if sm < k:
            return 0

        def amountPile(v):
            res = 0
            for i in candies:
                res += i // v

            return res >= k

        l, r = 1, sm // k
        res = 0

        while l <= r:
            m = (l + r) // 2
            if amountPile(m):
                res = max(res, m)
                l = m + 1

            else:
                r = m - 1

        return res