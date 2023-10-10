class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        slide = 0
        s = s[:: -1]
        pointer = k - 1
        resL, resR = 0, 0
        
        for i in range(k):
            slide += ((ord(s[i]) - 96) * pow(power, pointer, modulo))
            pointer -= 1
            
        leftPointer, rightPointer = 0, k
        
        while rightPointer < len(s):
           
            if slide % modulo == hashValue:
             
                resL, resR = leftPointer, rightPointer
                
            
            slide -= ((ord(s[leftPointer]) - 96) * pow(power, k - 1, modulo))
            slide *= (power )
            slide += ((ord(s[rightPointer]) - 96) )
            slide = slide % modulo
            leftPointer += 1
            rightPointer += 1
            
        if slide % modulo == hashValue:
            resL, resR = leftPointer, rightPointer

            
        temp = s[resL: resR]
        return temp[::-1]