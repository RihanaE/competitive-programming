class Solution:
    def minDeletions(self, s: str) -> int:
        num = Counter(s)
        ls = [[i, num[i]] for i in num]
        ls.sort(key = lambda k:k[1])
        pointer = len(ls) - 2
        ans = 0
        
        while pointer >= 0:
            if ls[pointer][1] == ls[pointer + 1][1]:
                while ls[pointer][1] == ls[pointer + 1][1] and ls[pointer][1] != 0:
                    ls[pointer][1] -= 1
                    ans += 1
                    ls.sort(key = lambda k:k[1])
            
            pointer -= 1
            
        return ans