class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        i=1
        j=1
        
        res=0
        
        for i in range(1,r - 1):
            for j in range(1,c - 1):
                s=grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                
                res=max(s,res)
                
        return res