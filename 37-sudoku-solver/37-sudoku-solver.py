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
            for r in range(n):
                for c in range(n):
                    if board[r][c]==".":
                        for no in range(1,10):
                            if isPossible(r,c,str(no)):
                                board[r][c]=str(no)
                                if solve(board):
                                    return True
                                board[r][c]="."
                        return False
            return True
                    
        n=len(board)
        solve(board)
        return board
        
        