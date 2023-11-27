class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = digits[-1] + 1
        
        if temp >= 10 - 1:
            pointer = len(digits) - 1
            
            while temp >= 10 and pointer >= 0:
                digits[pointer] = temp % 10
                pointer -= 1
                
                if pointer >= 0:
                    temp = digits[pointer] + 1
                
            if temp >= 10 and pointer == -1:
                digits[pointer] = temp % 10
                digits = [temp // 10] + digits
                
            elif temp >= 10:
                digits = [temp // 10] + [temp % 10] + digits
                
            else:
                digits[pointer] = temp
                
        else:
            digits[-1] = temp
            
        return digits