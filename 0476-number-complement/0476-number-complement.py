class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num)) - 2
        
        temp = 2 ** length - 1
        
        return ~num & temp