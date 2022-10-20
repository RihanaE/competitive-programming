class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp = {}
        stack = []
        for i in p:
            if i not in dp.keys():
                dp[i] = 1

            else:
                dp[i] += 1

        l, r = 0, 0
        ds = {}
        while r <= len(s):
            if r < len(s) and r - l < len(p):
                if s[r] not in ds.keys():
                    ds[s[r]] = 1

                else:
                    ds[s[r]] += 1

                r += 1

            elif r - l == len(p):
                if ds == dp:
                    stack.append(l)
                    if ds[s[l]] == 1:
                        del ds[s[l]]

                    else:
                        ds[s[l]] -= 1

                    l += 1

                   
                else:
                    if ds[s[l]] == 1:
                        del ds[s[l]]

                    else:
                        ds[s[l]] -= 1

                    l += 1
                   
            else:
                r +=1
                
        return stack