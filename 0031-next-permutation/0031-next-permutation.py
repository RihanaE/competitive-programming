class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            return nums.reverse()
        
        l=len(nums) - 2
        
        while l >= 0 and nums[l] >= nums[l + 1]:
            l -=1
            
        if l == -1:
            return nums.sort()
        
        else:
            r=len(nums) - 1
            
            while nums[l] >= nums[r]:
                r -=1
                
            nums[l], nums[r]=nums[r] , nums[l]
            nums[l + 1:]= reversed(nums[l + 1:])