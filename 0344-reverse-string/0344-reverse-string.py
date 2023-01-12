class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_pointer = 0
        right_pointer = len(s) - 1
        
        while left_pointer <= right_pointer:
            temp = s[right_pointer]
            s[right_pointer] = s[left_pointer]
            s[left_pointer] = temp
            left_pointer += 1
            right_pointer -= 1