class Solution:
    def addDigits(self, num: int) -> int:
        no = 0
        
        while len(str(num)) != 1:

            while num:
                no += num % 10
                num = num // 10
                
            num = no
            no = 0
            
        return num