class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] =0
                
            else:
                nums[i]=1
                
        s=0
        l=0
        res=0
        d={0 : 1}
        
        while l < len(nums):
            s +=nums[l]
            
            if s - k in d.keys():
                res +=d[s - k]
                
            if s in d.keys():
                d[s] +=1
                
            else:
                d[s]=1
                
            l +=1
            
        return res