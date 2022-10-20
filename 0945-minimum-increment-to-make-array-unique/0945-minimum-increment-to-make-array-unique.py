class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        d={}
        p=0
        count=0
        nums.sort()
        
        while p < len(nums):
            if nums[p] not in d.keys():
                d[nums[p]]=1
                p +=1
                
            elif nums[p] in d.keys():
                temp=nums[p - 1] - nums[p] + 1
                count +=temp
                nums[p] +=temp
                
        return count