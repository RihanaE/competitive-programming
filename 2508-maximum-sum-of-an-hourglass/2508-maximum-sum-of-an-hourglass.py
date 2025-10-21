class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        def ligit(rw, cl):
            return 0 <= rw < r and 0 <= cl <c

        def mx_sm(rw, cl):
            sm = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1] +grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
            return sm

        res = 0
        for i in range(r):
            for j in range(c):
                if ligit(i + 2, j + 2):
                    res = max(res, mx_sm(i, j))

        return res