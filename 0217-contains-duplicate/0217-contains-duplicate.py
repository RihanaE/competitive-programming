class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i=1
        count=0 
        
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                count +=1
                
            i +=1
            
        return count != 0