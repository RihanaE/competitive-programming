class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k=1
        l, r= 0 , 0
        count, res=0 , 0
        
        if 0 not in nums:
            return len(nums) - 1
        
        while r < len(nums):
            if nums[r] == 1:
                count +=1
                r +=1
                
            elif k > 0 and nums[r] == 0:
                r +=1
                k -=1
                
            elif k == 0:
                res=max(res,count)
                if nums[l] == 0:
                    k +=1
                    l +=1
                    
                else:
                    l +=1
                    count -=1
        
        res=max(res,count)
        
        return res