# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        leftPointer = 0
        rightPointer = n
        
        while leftPointer <= rightPointer:
            num = (leftPointer + rightPointer) // 2
           
            if guess(num) == 0:
                return num
            
            elif guess(num) == -1:
                rightPointer = num - 1
                
            else:
                leftPointer = num + 1