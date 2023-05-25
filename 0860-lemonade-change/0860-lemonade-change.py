class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5:
            return False
        
        no_five = 0
        no_ten = 0
        no_twenty = 0
        
        for bill in bills:
            if bill - 5 == 0:
                no_five += 1
                
            elif bill - 5 == 5 and no_five > 0:
                no_ten += 1
                no_five -= 1
                
            elif bill - 5 == 15 and no_five > 0 and (no_ten > 0 or no_five > 2):
                if no_ten > 0:
                    no_five -= 1
                    no_ten -= 1
                    no_twenty += 1
                    
                else:
                    no_five -= 3
                    no_twenty += 1
                    
            else:
                return False
            
        return True