class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        candidate = set()
        queue = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == len(board) - 1 or i == 0:
                    if board[i][j] == "O" and (i, j) not in queue:
                        queue.append((i, j))
                        
                elif j == len(board[0]) - 1 or j == 0:
                    if board[i][j] == "O" and (i, j) not in queue:
                        queue.append((i, j))
                        
                        
        while queue:
            node_rw, node_col = queue.popleft()
            candidate.add((node_rw, node_col))
            
            for r, c in directions:
                nw_rw = node_rw + r
                nw_col = node_col + c
                
                if inbound(nw_rw, nw_col) and board[nw_rw][nw_col] == "O" and (nw_rw, nw_col) not in candidate:
                    queue.append((nw_rw, nw_col))
                    
        
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in candidate:
                    board[i][j] = "X"
                    
        return board