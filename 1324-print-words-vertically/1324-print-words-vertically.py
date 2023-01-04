class Solution:
    def printVertically(self, s: str) -> List[str]:
        store = list((s.split()))
        output = []
        amount = 0

        for i in range(len(store)):
            if len(store[i]) > amount:
                amount = len(store[i])

        for i in range(amount):
            s = []
            for j in range(len(store)):
                if i < len(store[j]):
                    s.append(store[j][i])

                else:
                    s.append(" ")
                    
            s="".join(s)

            output.append(s.rstrip())

        return output
 
