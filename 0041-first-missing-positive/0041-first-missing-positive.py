class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                
        for i in range(len(nums)):
            res = abs(nums[i])
            if 1 <= res <= len(nums):
                if nums[res - 1] > 0:
                    nums[res - 1] *= -1
                    
                elif nums[res - 1] == 0:
                    nums[res - 1] = -1 * (len(nums) + 1)
                    
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
            
        return len(nums) + 1