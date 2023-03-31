class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        length = len(bin(n)) - 2
        if length == 1:
            return True
        
        else:
            flag = None
            for i in range(length):
        
                if n >> i & 1 == 1 and (flag == False or flag == None):
                    flag = True
                    
                    
                elif n >> i & 1 == 0 and (flag == True or flag == None):
                    flag = False
                    
                else:
                    return False
                
            return True