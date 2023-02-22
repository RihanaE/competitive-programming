class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        else:
            left = 0
            curr = 0
            res = len(nums)
            
            for right in range(len(nums)):
                curr += nums[right]
                
                while curr >= target:
                    res = min(res, right - left + 1)
                    curr -= nums[left]
                    left += 1
                    
            return res