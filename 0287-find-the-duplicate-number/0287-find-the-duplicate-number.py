class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pointer = 0
        
        while pointer < len(nums):
            place = nums[pointer] - 1
            
            if nums[pointer] == nums[place] and pointer != place:
                return nums[pointer]
            
            elif place == pointer:
                pointer += 1
                
            else:
                nums[pointer], nums[place] = nums[place], nums[pointer]
                
        