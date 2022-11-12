class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        res = 0
        l, r = 0, 0

        while r < len(nums):
            if s < target:
                s += nums[r]
                r += 1

            if s >= target:
                while s >= target:
                    if res == 0:
                        res = r - l
                    else:
                        res = min(res, r - l)

                    s -= nums[l]
                    l += 1
        
        return res