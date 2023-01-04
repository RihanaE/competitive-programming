class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        compare1=self.transpose_maker(grid)
        count=0
        
        for i in compare1:
            for j in grid:
                if i == j:
                    count +=1
                    
        return count
        
        
    
    
    def transpose_maker(self, grid):
        length=len(grid)
        output=[]
        for i in range(length):
            output.append([0]*length)
        
        for i in range(length):
            for j in range(length):
                output[i][j] = grid[j][i]
                
                
        return output