class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        
        res = float('inf')
        left = 0
        right = len(nums) - 1
        
        for i in range(4):
            
            res = min(res, nums[right - (3 - i)] - nums[left + i])
            
        return res
            

        