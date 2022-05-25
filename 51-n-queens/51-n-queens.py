class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isPossible(row,col):
            #check top-bottom
            for i in range(row):
                if visited[i][col]:
                    return False
            #right diagonal
            i=row
            j=col
            while i>=0 and j<n:
                if visited[i][j]:
                    return False
                i-=1
                j+=1
            #left diagonal
            i=row
            j=col
            while i>=0 and j>=0:
                if visited[i][j]:
                    return False
                i-=1
                j-=1
            return True
            
        
        def solve(row):
            if row==n:
                temp=[]
                string=""
                for i in range(n):
                    for j in range(n):
                        if visited[i][j]:
                            string+="Q"
                        else:
                            string+="."
                    
                    temp.append(string)
                    string=""
                res.append(temp)
                
                
            
            for col in range(n):
                if isPossible(row,col):
                    visited[row][col]=True
                    solve(row+1)
                    visited[row][col]=False
            
        visited=[[False for col in range(n)] for row in range(n)]
        res=[]
        solve(0)
        return res
        