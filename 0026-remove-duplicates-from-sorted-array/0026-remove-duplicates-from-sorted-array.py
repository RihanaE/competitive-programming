class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = 1
        count = 0
        
        while right_pointer < len(nums):
            if nums[left_pointer] == nums[right_pointer]:
                nums[left_pointer] = 101
                left_pointer += 1
                right_pointer += 1
                
            else:
                left_pointer += 1
                right_pointer += 1
                
        left_pointer = 0
        right_pointer = 1
        
        while right_pointer < len(nums):
            if nums[left_pointer] == 101 and nums[right_pointer] != 101:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                
            elif nums[right_pointer] == 101:
                right_pointer += 1
                
            elif left_pointer < right_pointer - 1 and nums[left_pointer] != 101:
                left_pointer += 1
                
                
            else:
                right_pointer += 1
                
                
        for i in nums:
            if i != 101:
                count += 1
        return count