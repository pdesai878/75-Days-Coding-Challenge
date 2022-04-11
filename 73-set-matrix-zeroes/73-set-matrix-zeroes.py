class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:         
        row,col=set(),set()
        n=len(matrix) #rows
        m=len(matrix[0]) #cols
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
                    
        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    matrix[i][j]=0
        
        return matrix
        
                