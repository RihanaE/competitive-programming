class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left_pointer = 0
        # right_pointer = self.give(c)
        right_pointer = int(c ** 0.5)
        
        while left_pointer <= right_pointer:
            if (left_pointer ** 2) + (right_pointer ** 2) == c:
                return True
            
            elif  (left_pointer ** 2) + (right_pointer ** 2) < c:
                left_pointer += 1
                
            elif  (left_pointer ** 2) + (right_pointer ** 2) > c:
                right_pointer -= 1
                
        return False
    
#     def give(c):
#         temp = c // 2 + 1
        
#         if temp ** 2 > c:
#             temp = temp // 2 + 1