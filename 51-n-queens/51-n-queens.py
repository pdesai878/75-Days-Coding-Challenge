class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isPossible(row,col):
            #check top-bottom
            for i in range(row):
                if visited[i][col]=="Q":
                    return False
            #right diagonal
            i=row
            j=col
            while i>=0 and j<n:
                if visited[i][j]=="Q":
                    return False
                i-=1
                j+=1
            #left diagonal
            i=row
            j=col
            while i>=0 and j>=0:
                if visited[i][j]=="Q":
                    return False
                i-=1
                j-=1
            return True
            
        
        def solve(row):
            if row==n:
                temp=[]
                for r in visited:
                    temp.append("".join(r))
                    
                res.append(temp)
                      
            
            for col in range(n):
                if isPossible(row,col):
                    visited[row][col]="Q"
                    solve(row+1)
                    visited[row][col]="."
            
        visited=[["." for col in range(n)] for row in range(n)]
        res=[]
        solve(0)
        return res
        