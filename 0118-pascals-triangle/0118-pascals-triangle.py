class Solution:
    def generate(self, numsRows: int) -> List[List[int]]:
        if numsRows == 1:
            return [[1]]
        elif numsRows == 2:
            return [[1], [1, 1]]

        else:
            output = [[1], [1, 1]]
            n = numsRows - 2

            for i in range(2, numsRows):
                l = i
                s = []
                j = 0
                while l >= 0:
                    if s == []:
                        s.append(output[i - 1][j])

                    elif 0 < j < i:
                        s.append(output[i - 1][j] + output[i - 1][j - 1])

                    else:
                        s.append(output[i - 1][-1])

                    l -= 1
                    j += 1

                output.append(s)

        return output
