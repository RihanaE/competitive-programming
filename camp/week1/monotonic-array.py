class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = None
        leftPointer = 1
        
        while leftPointer < len(nums):
            if nums[leftPointer - 1] < nums[leftPointer] and flag == None:
                flag = True # monotone increasing array
                
            elif nums[leftPointer - 1] > nums[leftPointer] and flag == None:
                flag = False # decreasing array
                
            elif nums[leftPointer - 1] < nums[leftPointer] and not flag:
                return False
            
            elif nums[leftPointer - 1] > nums[leftPointer] and flag:
                return False
            
            leftPointer += 1
            
        return True