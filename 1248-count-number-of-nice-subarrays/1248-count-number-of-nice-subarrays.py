class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        store = {0 : 1}
        res = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
                
            else:
                nums[i] = 1
                
        for i in range(1 , len(nums)):
            nums[i] += nums[i - 1]
            
        for i in nums:
            if i - k in store:
                res += store[i - k]
                
            if i in store:
                store[i] += 1
                
            else:
                store[i] = 1
                
        return res
        