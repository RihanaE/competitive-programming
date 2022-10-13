class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range (len(nums)):
            if nums[i] % 2 == 0:
                nums[i] =0
                
            else:
                nums[i]=1
                
        d={0:1}
        t=0
        res=0
        
        for i in nums:
            t +=i
           
            if t - k in d.keys():
                res +=d[t - k]
                
            if t in d.keys():
                d[t] +=1
                
            else:
                d[t] =1
                
        return res