class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    def dfs(self, board, )    
        
        
        
        
    def valid(self, board, r, c, val):
        for i in range(10):
            if board[i][c] == val:
                return False
            
        for i in range(10):
            if board[r][i] == val:
                return False
            
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if board[i][j] == val:
                    return False
        return True