class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = "aeiou"
        n = k
        l, r = 0, 0
        check = 0
        res = 0

        while l <= len(s) - k:
            if n > 0:
                if r < len(s) and s[r] in v:
                    check += 1
                    n -= 1
                    r += 1
                else:
                    n -= 1
                    r += 1

            else:
                res = max(res, check)
                if s[l] in v:
                    check -= 1

                if r < len(s) and s[r] in v:
                    check += 1

                l += 1
                r += 1

        #res = max(res, check)

        if res > k:
            return k
        else:
            return res
