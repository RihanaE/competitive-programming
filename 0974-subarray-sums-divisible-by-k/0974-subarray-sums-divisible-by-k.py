class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store = { 0 : 1}
        res = 0

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for i in nums:
            if (i - k) % k in store:
                res += store[(i - k) % k]

            if i % k in store:
                store[i % k] += 1

            else:
                store[i % k ] = 1

        return res