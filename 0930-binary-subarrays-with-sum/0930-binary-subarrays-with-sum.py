class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i]+= nums[i - 1]
            
        store = {0 : 1}
        res = 0
        
        for i in nums:
            if i - k in store:
                res += store[i - k]
                
            if i in store:
                store[i] += 1
                
            else:
                store[i] = 1
                
        return res