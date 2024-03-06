class Solution:
    def isUgly(self, n: int) -> bool:
        choice = [2, 3, 5]
        pointer = 0
        d = 2
        
        if n <= 0:
            return False
        
        while n != 1:
            while n % d == 0:
                n = n // d
                
            pointer += 1
            if pointer > 2 and n != 1:
                return False
            
            elif pointer <= 2:
                d = choice[pointer]
            
        return True