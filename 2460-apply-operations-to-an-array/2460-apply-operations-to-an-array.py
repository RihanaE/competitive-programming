class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] = nums[i - 1] * 2
                nums[i] = 0

        left_pointer = 0
        right_pointer = 0

        while right_pointer < len(nums) and left_pointer < len(nums):
            if nums[left_pointer] == 0 and nums[right_pointer] != 0 and right_pointer > left_pointer:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer += 1
                right_pointer += 1

            elif nums[right_pointer] != 0 and right_pointer < left_pointer:
                right_pointer +=1

            elif nums[right_pointer] == 0:
                right_pointer += 1

            elif nums[left_pointer] != 0:
                left_pointer += 1

        return nums
