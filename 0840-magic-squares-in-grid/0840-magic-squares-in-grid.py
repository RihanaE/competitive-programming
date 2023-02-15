class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        l = 0
        r = 2
        t = 0
        b = 2
        count = 0
        
        while r < len(grid[0]):
            
            if self.checker(grid, l, r, t, b):
                if self.col_sum(grid,l, r, t, b) == self.row_sum(grid, l, r, t) == self.diagonal_sum(grid, l, r, t) != False:
                    count += 1
                
            t += 1
            b += 1
            
            if b == len(grid):
                r += 1
                l += 1
                t = 0
                b = 2
            
        return count
            
    def row_sum(self, grid,l , r , t):
        temp = []

        for i in range(3):
            if temp != []:
                if sum(grid[t][l: r + 1]) != temp[-1]:
                    return False

            else:
                temp.append(sum(grid[t][l: r + 1]))

            t += 1

        return temp[-1], True
    
    def col_sum(self, grid, l, r, t, b):
        temp = []
        start = t


        for i in range(3):
            temp1 = 0
            t = start
            for j in range(3):
                temp1 += grid[t][l]
                t += 1

            if temp != []:
                if temp1 != temp[-1]:
                    return False

            else:
                temp.append(temp1)

            l += 1

        return temp[-1], True

    
    def diagonal_sum(self, grid, l, r, t):
        start = l - t
        start_t = t
        end = r + t
        temp1 = 0
        temp2 = 0


        for i in range(3):
            if start == l - t:
                temp1 += grid[t][l]

            t += 1
            l += 1

        t = start_t
        for i in range(3):
            if end == r + t:
                temp2 += grid[t][r]

            t += 1
            r -= 1

        if temp1 != temp2:
            return False

        else:
            return temp1, True
        
        
    def checker(self, grid, l, r, t, b):
        res = []
        
        for j in range(t, b + 1):
            for i in range(3):
                if grid[j][l + i] > 9 or grid[j][l + i] < 1:
                    return False
                
                res.append(grid[j][l + i])
            
        if len(res) != len(set(res)):
            return False
        
        return True