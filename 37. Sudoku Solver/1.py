class Solution:
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board, 0,0)
        
    def dfs(self, board, r, c):
        while board[r][c] != ".":
            c += 1
            if c == 9:
                r += 1
                c = 0
            if r == 9:
                return True
            
        for i in range(1, 10):
            tmp = str(i)
            if self.valid(board, r, c, tmp):
                board[r][c] = tmp
                if self.dfs(board, r, c):
                    return True
        board[r][c] = "."
        return False
        
    def valid(self, board, r, c, val):
        for i in range(9):
            if board[i][c] == val:
                return False
            
        for i in range(9):
            if board[r][i] == val:
                return False
            
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if board[i][j] == val:
                    return False
        return True