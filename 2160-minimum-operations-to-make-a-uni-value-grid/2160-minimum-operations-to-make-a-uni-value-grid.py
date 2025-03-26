class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ls = []
    
        mod = grid[0][0] % x
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] % x != mod:
                    return -1

                ls.append(grid[m][n])

        ls.sort()
        pre = ls[:]
        for i in range(1, len(pre)):
            pre[i] += pre[i - 1]

        mn = float(inf)
        l = len(ls)
        print(pre)
        print(ls)
        for i in range(len(ls)):
            if i == 0:
                af = (pre[l - 1] - (ls[i] * (l - i))) // x
                mn = min(af, mn)
            elif i == l - 1:
                bf = ((ls[i] * i) - pre[i - 1]) // x
                mn = min(bf, mn)
            else:
                bf = ((ls[i] * i) - pre[i - 1]) // x
                af = (pre[l - 1] - pre[i - 1] - (ls[i] * (l - i))) // x
                mn = min(bf + af, mn)

        return mn
        4 - 2 // 2 + 20 - 2 - 12 // 2
        1 + 2