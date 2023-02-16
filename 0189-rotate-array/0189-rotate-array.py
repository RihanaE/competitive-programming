class Solution:
    def rotate(self, nums: List[int], n: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=n % len(nums)
        l=0
        r=len(nums) - k - 1
        
        while l <= r:
            nums[l], nums[r]=nums[r] , nums[l]
            l +=1
            r -=1
            
        l, r=len(nums) - k, len(nums) - 1
        
        while l <= r:
            nums[l], nums[r]=nums[r] , nums[l]
            l +=1
            r -=1
            
        l=0
        r=len(nums) - 1
        while l <= r:
            nums[l], nums[r]=nums[r] , nums[l]
            l +=1
            r -=1