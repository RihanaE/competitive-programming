class Solution:
    def reverseVowels(self, s: str) -> str:
        leftPointer = 0
        rightPointer = len(s) - 1
        store = set({"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"})
        s = [i for i in s]
        
        while leftPointer <= rightPointer:
            if s[leftPointer] in store and s[rightPointer] in store:
                s[leftPointer], s[rightPointer] = s[rightPointer], s[leftPointer]
                leftPointer += 1
                rightPointer -= 1
                
            elif s[leftPointer] not in store:
                leftPointer += 1
                
            elif s[rightPointer] not in store:
                rightPointer -= 1
                
        res = "".join(s)
        return res