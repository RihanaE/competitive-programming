class Solution:
    def reverseString(self,  s ,c = 0) :
        """
        Do not return anything, modify s in-place instead.
        """
        left_pointer = 0 + c
        right_pointer = len(s) - 1 - c
        
        if left_pointer >= right_pointer:
            return s
        
        else:
            
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            
            return self.reverseString( s , c + 1)