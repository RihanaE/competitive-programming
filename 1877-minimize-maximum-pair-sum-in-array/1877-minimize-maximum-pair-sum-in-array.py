class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums) -1
        max_no=0
        
        while i < j:
            max_no=max(max_no, nums[i] + nums[j])
            
            i+=1
            j-=1
           
            

        return max_no

        