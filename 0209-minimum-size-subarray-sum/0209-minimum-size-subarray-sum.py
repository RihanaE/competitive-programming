class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        res = float("inf")
        
        for right in range(len(nums)):
            curr += nums[right]
            
            if curr >= target:
                while curr >= target:
                    res = min(res, right - left + 1)
                    curr -= nums[left]
                    left += 1
                    
            right += 1
            
        if res != float("inf"):
            return res
        return 0