class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        check = 0

        for i in range(len(nums)):
            if i > 0:
                check += nums[i - 1]
            t =s - check - nums[i]

            if check == t:
                return i 

        else:
            return -1
