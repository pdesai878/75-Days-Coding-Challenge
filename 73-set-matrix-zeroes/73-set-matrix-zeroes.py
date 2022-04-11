class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:         
        n=len(matrix) #rows
        m=len(matrix[0]) #cols
        
        isCol=False
        for i in range(n):
            if matrix[i][0]==0:
                isCol=True
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                                
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
                    
        if matrix[0][0]==0:
            for col in range(m):
                matrix[0][col]=0
        if isCol:
            for row in range(n):
                matrix[row][0]=0
        return matrix
        
                