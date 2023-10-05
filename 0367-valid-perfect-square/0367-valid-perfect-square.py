class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        leftPointer = 0
        rightPointer = num
        
        while leftPointer <= rightPointer:
            no = (leftPointer + rightPointer) // 2
            if no * no == num:
                return True
            
            elif no * no > num:
                rightPointer = no - 1
                
            else:
                leftPointer = no + 1
                
        return False