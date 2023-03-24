class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        pointer = 0
        res = []
        while pointer < len(nums):
            place = nums[pointer] - 1
            
            if nums[place] == nums[pointer] and place != pointer:
                if nums[pointer] not in res:
                    res.append(nums[pointer])
                    
                pointer += 1
                
                
            elif place == pointer:
                pointer += 1
                
                
            else:
                nums[place], nums[pointer] = nums[pointer], nums[place]
                
        return res