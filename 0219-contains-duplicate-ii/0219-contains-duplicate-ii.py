class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        l, r = 0, 1

        if len(nums) == len(set(nums)):
            return False
        
        if k == 0 or len(nums) == 1:
            return False

        while r < len(nums):
            if r - l <= k:
                if nums[l] in nums[l + 1:r + 1] or nums[r] in nums[l : r]:
                    return True

                elif nums[l] not in nums[l + 1:r + 1] and r - l < k:
                    r += 1

            if nums[l] not in nums[l + 1:r + 1] and r - l == k:
                l += 1
                r += 1

        else:
            return False