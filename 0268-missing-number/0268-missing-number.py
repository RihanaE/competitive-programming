class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pointer = 0
        track = {}
        
        while pointer < len(nums):
            place = nums[pointer] - 1
            
            if nums[pointer] == 0:
                track[0] = pointer
                pointer += 1
                
                
            elif place == pointer:
                pointer += 1
                
            else:
                nums[pointer], nums[place] = nums[place], nums[pointer]
                
        
        if track:
            return track[0] + 1
        else:
            return 0