class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p1 = 0
        flag = False

        for i in range(len(strs[0])):
            a = strs[0][p1]

            for j in range(1, len(strs)):
                if p1 >= len(strs[j]) or a != strs[j][p1]:
                    flag = True
                    break

            if flag:
                break

            p1 += 1

        return strs[0][:p1]