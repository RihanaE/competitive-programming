class Solution:
    def reverseWords(self, s: str) -> str:
        leftPointer = 0
        rightPointer = 0
        store = []
        
        while rightPointer < len(s):
            temp = ""
            while rightPointer < len(s) and s[rightPointer] != " ":
                temp += s[rightPointer]
                rightPointer += 1
            
            if temp:
                store.append(temp[::-1])
                
            leftPointer = rightPointer + 1
            rightPointer += 1
                
                
        res = " ".join(store)
        return res