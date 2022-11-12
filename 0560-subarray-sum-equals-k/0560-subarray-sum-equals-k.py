class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0 : 1}
        l=0
        res=0
        s=0
        
        while l < len(nums):
            s +=nums[l]
            
            if s - k in d:
                res +=d[s - k]
                
            if s in d:
                d[s] +=1
            else:
                d[s] =1
                
            
                
            l+=1
            
        return res