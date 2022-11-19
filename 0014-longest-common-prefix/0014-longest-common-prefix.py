class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        j = 0
        l = 1

        if len(strs) == 1:
            return strs[0]

        while l <= len(strs[0]) + 1:
            if strs[0][:l] == strs[j][:l]:
                j += 1
                if j == len(strs):
                    res = strs[0][:l]
                    l += 1
                    j = 0

            elif l > len(strs[0]):
                return res

            else:
                return res

        return res