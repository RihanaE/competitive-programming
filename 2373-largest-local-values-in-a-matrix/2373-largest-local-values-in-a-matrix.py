class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        store = [[0] * (len(grid[0]) - 2)  for i in range(len(grid) - 2)] 
        l = 0
        r = 2
        t = 0
        b = 2
        row_pointer = 0
        col_pointer = 0
        
        while b < len(grid) and r < len(grid[0]):
            store[row_pointer][col_pointer] =  self.helper(grid, l, r , t, b)
            l += 1
            r += 1
            col_pointer += 1
            
            if col_pointer == len(grid) - 2:
                row_pointer += 1
                col_pointer = 0
                
            if r == len(grid[0]):
                t += 1
                b += 1
                l = 0
                r = 2
                
        return store
        
        
    def helper(self, grid, l ,r , t, b):
        temp = 0
        
        for i in range(t, b + 1):
            temp1 = max(grid[i][l: r + 1])
            temp = max(temp, temp1)
            
        return temp