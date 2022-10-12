class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        t=nums[0]
        l , r= 0 , 0
        res=len(nums)
        
        if sum(nums) < target:
            return 0
        
        while r < len(nums):
            if t < target:
                r +=1
                if r < len(nums):
                    t +=nums[r]
                
            if t >= target:
                res = min(res,r - l + 1)
                t -=nums[l]
                l +=1
                
        return res