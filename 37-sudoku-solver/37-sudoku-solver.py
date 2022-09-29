class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isPossible(r,c,no):
            #check row & col
            for i in range(9):
                if board[i][c]==no:
                    return False
                if board[r][i]==no:
                    return False
                #check in grid
                rgrid=3*(r//3)+i//3
                cgrid=3*(c//3)+i%3
                if board[rgrid][cgrid]==no:
                    return False
            return True
            
        def solve(board):
            for i in range(n):
                for j in range(n):
                    if board[i][j]=='.':
                        for no in range(1,10):
                            if isPossible(i,j,str(no)):
                                board[i][j]=str(no)
                                done=solve(board)
                                if done:
                                    return True
                                board[i][j]='.'
                        return False
            return True
                    
        n=9
        solve(board)
        return board
        
        