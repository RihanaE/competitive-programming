class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length  = len(nums)
        nums = sorted(set(nums))
        ans = length 
        rightPointer = 0
        
        for leftPointer in range(len(nums)):
            while rightPointer < len(nums) and nums[rightPointer] < nums[leftPointer] + length:
                rightPointer += 1
                
            slide = rightPointer - leftPointer
            ans = min(ans, length - slide)
            
        return ans