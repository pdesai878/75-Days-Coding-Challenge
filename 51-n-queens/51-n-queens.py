class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isPossible(r,c):
            #check col
            for i in range(n):
                if board[i][c]=="Q":
                    return False
            
            #check upper left diagonal
            i=r
            j=c
            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            
            #check upper right diagonal
            i=r
            j=c
            while i>=0 and j<n:
                if board[i][j]=="Q":
                    return False
                i-=1
                j+=1
            return True
                
            
        def nqueens(r):
            if r==n:
                temp=[]
                for row in board:
                    temp.append("".join(row))
                res.append(temp)
            
            for c in range(n):
                if isPossible(r,c):
                    board[r][c]="Q"
                    nqueens(r+1)
                    board[r][c]="."
   
         
        res=[]
        board=[["." for j in range(n)] for i in range(n)]
        nqueens(0)
        return res