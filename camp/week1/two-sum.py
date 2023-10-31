class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [[val, idx] for idx, val in enumerate(nums)]
        nums.sort()
        
        leftPointer = 0
        rightPointer = len(nums) - 1
        
        while leftPointer < rightPointer:
            if nums[leftPointer][0] + nums[rightPointer][0] > target:
                rightPointer -= 1
                
            elif nums[leftPointer][0] + nums[rightPointer][0] < target:
                leftPointer += 1
                
            else:
                return [nums[leftPointer][1], nums[rightPointer][1]]