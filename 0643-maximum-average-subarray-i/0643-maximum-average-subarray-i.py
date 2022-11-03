class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k - 1
        s=sum(nums[l:k])
        res=s/k
        
        
        while r < len(nums):
            s-=nums[l]
            l +=1
            r +=1
            if r < len(nums):
                s +=nums[r]
                res=max(res,s/k)
                
        return res