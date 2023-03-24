class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        track = {}
        pointer = 0
        
        while pointer < len(nums):
            place = nums[pointer] - 1
            
            if nums[pointer] == nums[place] and place != pointer:
                track[nums[pointer]] = pointer
                pointer += 1
                
            elif pointer == place:
                pointer += 1
                
            else:
                nums[pointer], nums[place] = nums[place], nums[pointer]
                
        for i in track.values():
            res.append(i + 1)
            
        return res