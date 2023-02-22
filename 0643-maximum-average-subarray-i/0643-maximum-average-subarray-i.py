class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -float("inf")
        store = 0
        left = 0
        
        for right in range(len(nums)):
            store += nums[right]
            
            if right - left == k - 1:
                res = max(store / k, res)
                store -= nums[left]
                left += 1
                
        return res