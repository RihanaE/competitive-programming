class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def whatTime(time_):
            res = 0
            for i in ranks:
                res += int((time_ / i) ** (1/2))

            return res

        l = 1
        r = ranks[0] * cars * cars
        res = r

        while l <= r:
            m = (l + r) // 2
            v = whatTime(m)
            if v >= cars:
                res = min(m, res)
                r = m - 1

            else:
                l = m + 1

        return res