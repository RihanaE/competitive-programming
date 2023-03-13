class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        
        if target in nums:
            res.append(bisect_left(nums, target))
            res.append(bisect_right(nums, target) - 1)
            
        else:
            return [-1, -1]

        return res