class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        sfirst = []
        ssecond = []
        l = 0
        while l + firstLen <= len(nums):
            sfirst.append(sum(nums[l: l + firstLen]))
            l += 1

        l = 0
        while l + secondLen <= len(nums):
            ssecond.append(sum(nums[l: l + secondLen]))
            l += 1

        res = 0
        po = firstLen
        r = 0
        for i in sfirst:

            r = po
            while r + secondLen <= len(nums):
                res = max(res, i + sum(nums[r: r + secondLen]))
                r += 1
            po += 1


        po = secondLen
        r = 0

        for i in ssecond:

            r = po
            while r + firstLen <= len(nums):
                res = max(res, i + sum(nums[r: r + firstLen]))
                r += 1

            po += 1


        return res
