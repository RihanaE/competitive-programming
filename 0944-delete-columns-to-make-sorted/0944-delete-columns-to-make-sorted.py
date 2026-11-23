class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        c = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j - 1][i]:
                    c += 1
                    break

        return c