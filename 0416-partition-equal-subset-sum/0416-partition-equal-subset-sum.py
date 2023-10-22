class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        
        @cache
        def backtrack(pointer, sm):
            if sm == target:
                return True
            
            elif sm > target:
                return False
            
            elif pointer >= len(nums):
                return False
            
            res = backtrack(pointer + 1, sm + nums[pointer]) or backtrack(pointer + 1, sm)
            return res
        
        return backtrack(0, 0)