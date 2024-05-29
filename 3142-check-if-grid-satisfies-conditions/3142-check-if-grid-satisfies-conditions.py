class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        def isBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        for rw in range(len(grid)):
            for cl in range(len(grid[0])):
                if (isBound(rw + 1, cl) and grid[rw][cl] != grid[rw + 1][cl]) or (isBound(rw, cl + 1) and grid[rw][cl] == grid[rw][cl + 1]):
                    return False
                
        return True