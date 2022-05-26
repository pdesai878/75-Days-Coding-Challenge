class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isPossible(no,row,col):
            for i in range(n):
                #check in row
                if board[row][i]==no:
                    return False
                #check in col
                if board[i][col]==no:
                    return False
                #check in grid
                curr_row_in_grid=3*(row//3)+i//3
                curr_col_in_grid=3*(col//3)+i%3
                if board[curr_row_in_grid][curr_col_in_grid]==no:
                    return False
            return True
        
        
        def solve(board):
            for i in range(n):
                for j in range(n):
                    if board[i][j]==".":
                        for no in range(1,10):
                            number=str(no)
                            if isPossible(number,i,j):
                                board[i][j]=number
                                done=solve(board)
                                if done:
                                    return True
                                else:
                                    board[i][j]="."
                        return False
            return True
        
        n=9
        solve(board)
        return board
        