class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(num) - 1
        
        while left_pointer < right_pointer:
            if num[left_pointer] + num[right_pointer] == target:
                return [left_pointer + 1, right_pointer + 1]
            
            elif num[left_pointer] + num[right_pointer] > target:
                right_pointer -= 1
                
            elif num[left_pointer] + num[right_pointer] < target:
                left_pointer += 1