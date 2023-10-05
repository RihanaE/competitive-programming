class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(nums) - 1
        count = 0
        
        if nums[leftPointer] > 0:
            return len(nums)
        
        elif nums[rightPointer] < 0 :
            return len(nums)
        
        for i in nums:
            if i == 0:
                count += 1
        
        while leftPointer < rightPointer:
            mid = (leftPointer + rightPointer) // 2
            if nums[mid] < 0:
                leftPointer = (mid + 1)
                
                
            else:
                rightPointer = (mid - 1)
        
        if nums[leftPointer] < 0:
            return max(leftPointer + 1, len(nums) - (leftPointer + 1) - count)
        
        return max(leftPointer, len(nums) - (leftPointer) - count)