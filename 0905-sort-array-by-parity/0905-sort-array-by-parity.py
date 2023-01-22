class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums) - 1
        
        while left_pointer <= right_pointer:
            if nums[left_pointer] % 2 == 0:
                left_pointer +=1
                
            elif nums[right_pointer] % 2 != 0:
                right_pointer -=1
                
            else:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer +=1
                right_pointer -= 1
                
        return nums