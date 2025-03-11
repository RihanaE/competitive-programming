class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        abcNum = defaultdict(int)
        res = 0

        for r in range(len(s)):
            abcNum[s[r]] += 1
            while len(abcNum) >= 3:
                res += len(s) - r
                abcNum[s[l]] -= 1

                if abcNum[s[l]] == 0:
                    abcNum.pop(s[l]) 
                l += 1

        return res