class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        down_one_sum = self.helper(grid)
        output = grid
        length = len(grid)
        length_col = len(grid[0])
        
        for i in range(len(grid)):
            no_of_one = sum(grid[i])
            no_of_zero = length_col - no_of_one
            
            pointer = 0
            
            while pointer < length_col:
                no_of_zero2 = length - down_one_sum[pointer]
                output[i][pointer] = no_of_one + down_one_sum[pointer] - no_of_zero - no_of_zero2
                pointer += 1
                
        return output
                
            
#         length = len(grid)
#         length_row = len(grid[0])
#         store = []
        
        
#         for i in range(len(grid)):
#             no_of_one = sum(grid[i])
#             no_of_zero = len(grid[0]) - no_of_one
#             output = []
            
#             for j in range(len(grid[0])):
#                 no_of_one2 = self.helper(grid, j)
#                 no_of_zero2 = len(grid) - no_of_one2
#                 answer = no_of_one + no_of_one2 - no_of_zero - no_of_zero2
#                 output.append(answer)
                
#             store.append(output)
            
            
#         return store
    
    def helper(self,grid):
        result = {}
        length = len(grid)
        length_col = len(grid[0])
        answer=0
        
        for i in range(length_col):
            for j in range(length):
                answer += grid[j][i]
                
            result[i] = answer
            answer = 0
            
        return result
    
    
            
#     def helper(self, grid, column_no):
#         result = 0
        
#         for i in range(len(grid)):
#             result += grid[i][column_no]
            
#         return result