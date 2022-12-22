class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i=0
        j=1
        length=len(nums)
        count=0
        
        while i < length - 1:
            if nums[i] == nums[j]:
                count +=1
                
            j +=1
            if j == length:
                i +=1
                j =i + 1
                
        return count