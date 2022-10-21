class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l= 0
        res=0
        count=0
        
        while l < len(nums):
            if nums[l] == 1:
                count +=1
                
            else:
                res=max(res,count)
                count=0
                
            l +=1
       
        res=max(res,count)   
        
        return res