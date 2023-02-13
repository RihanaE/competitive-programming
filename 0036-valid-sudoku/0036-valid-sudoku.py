class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.col_helper(board) == self.row_helper(board) == self.three_helper(board) == True:
            return True
        
        return False
        
        
    def col_helper(self, board):
        for i in range(len(board[0])):
            store = []
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in store:
                    return False
                
                store.append(board[j][i])
            
        return True
            
            
    def row_helper(self, board):
        for i in range(len(board)):
            store = []
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in store:
                    return False
                    
                store.append(board[i][j])
            
        return True
    
    def three_helper(self, grid):
        t = 0  
        l = 0
        r = 2
        
        
        while t < len(grid) and r < len(grid[0]):
            value = self.checker(grid, t, l, r)
            if value == False:
                return False
            
            t += 3
            if t == len(grid):
                l += 3
                r += 3
                t = 0
                
        return True
                
            
            
            
            
    def checker(self, grid, t, l, r):
        temp=[]
        for i in range(3):
            for i in grid[t][l : r + 1]:
                if i > "9":
                    return False

                if i != "." and i in temp:
                    return False

                temp.append(i)
                
            t += 1
            
            
        return True