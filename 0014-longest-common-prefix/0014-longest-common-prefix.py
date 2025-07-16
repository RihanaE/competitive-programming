class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        lim = len(strs[0])

        for i in range(lim):
            w = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return res

                elif w != strs[j][i]:
                    return res

            res += w

        return res