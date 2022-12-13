class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def getMin(i,j):
            if j>=col or j<0:
                return sys.maxsize
            
            if i==row-1:
                return matrix[i][j]
            
            down=getMin(i+1,j)
            left_diag=getMin(i+1,j-1)
            right_diag=getMin(i+1,j+1)
            
            return min(down,left_diag,right_diag)+matrix[i][j]
            
        
        row=col=len(matrix)
        mn=sys.maxsize
        for j in range(col):
            mn=min(mn,getMin(0,j))
        return mn
            
        