class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        track = {}
        pointer = 0
        res = []
        temp = 0
        
        while pointer < len(nums):
            place = nums[pointer] - 1
            
            if nums[pointer] == nums[place] and place != pointer:
                if nums[pointer] not in track:
                    temp = nums[pointer]
                    res.append(nums[pointer])
                    
                track[nums[pointer]] = pointer
                pointer += 1
                
            elif pointer == place:
                pointer += 1
                
            else:
                nums[pointer], nums[place] = nums[place], nums[pointer]
                

        res.append(track[temp] + 1)
            
        return res