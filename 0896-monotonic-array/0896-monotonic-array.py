class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        leftPointer = 0
        rightPointer = 1
        inc = True
        dec = True
        
        if len(nums) <= 1:
            return True
        
        while rightPointer < len(nums):
            if nums[rightPointer] < nums[leftPointer]:
                dec = False
                
            elif nums[rightPointer] > nums[leftPointer]:
                inc = False
                
            leftPointer += 1
            rightPointer += 1
            
        if not inc and not dec:
            return False
        
        return True