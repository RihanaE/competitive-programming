class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        store = [0] * len(s)
        temp = []

        for i in s:
            temp.append(ord(i) - 97)

        for shift in shifts:
            i, j, k = shift

            if k == 0:
                store[i] -= 1

                if j < len(s) - 1:
                    store[j + 1] += 1

            elif k == 1:
                store[i] += 1

                if j < len(s) - 1:
                    store[j + 1] -= 1
    
        
        for i in range(1, len(s)):
            store[i] += store[i - 1]

        for i in range(len(s)):
            store[i] += temp[i]
        
        for i in range(len(store)):
            store[i] = chr((store[i] % 26) + 97)

        return "".join(store)