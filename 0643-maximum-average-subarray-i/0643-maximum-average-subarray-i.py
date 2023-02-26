class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -float("inf")
        left = 0
        right = 0
        curr = 0
        
        while right < len(nums):
            curr += nums[right]
            if right - left == k - 1:
                res = max(res, curr/k)
                curr -= nums[left]
                left += 1
                
            right += 1
            
        return res