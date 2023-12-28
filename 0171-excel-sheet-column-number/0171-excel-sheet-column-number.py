class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        diction = {}
        res = 0
        
        pointer = ord("A")
        
        for i in range(1, 27):
            diction[chr(pointer)] = i
            pointer +=1
            
        length = len(columnTitle)
        
        for i in columnTitle:
            res += (diction[i] * (26 ** (length - 1)))
            length -= 1
            
        return res