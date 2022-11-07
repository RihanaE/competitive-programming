class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        s = 0
        l = 0
        res = 0

        while l < len(nums):
            s += nums[l]
            if s - k in d.keys():
                res += d[s - k]

            if s in d.keys():
                d[s] += 1

            else:
                d[s] = 1

            l += 1

        return res