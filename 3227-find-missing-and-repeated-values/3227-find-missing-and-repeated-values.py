class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        length = len(grid) * len(grid[0])
        values = [-1] * length
        ans = []
        num = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num += 1

                if values[grid[i][j] - 1] != -1:
                    ans.append(grid[i][j])

                else:
                    values[grid[i][j] - 1] = grid[i][j]

        ans.append(values.index(-1) + 1)
        return ans