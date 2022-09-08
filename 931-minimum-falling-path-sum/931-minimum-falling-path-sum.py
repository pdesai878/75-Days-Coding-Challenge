class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def getMin(i,j):
            if i>=n or j>=n or j<0:
                return sys.maxsize
            if i==n-1:
                return matrix[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            down=getMin(i+1,j)+matrix[i][j]
            left_diag=getMin(i+1,j-1)+matrix[i][j]
            right_diag=getMin(i+1,j+1)+matrix[i][j]
            dp[i][j]=min(down,left_diag,right_diag)
            return dp[i][j]
        
        n=len(matrix)
        mn=sys.maxsize
        dp=[[-1 for j in range(n)]for i in range(n)]
        for i in range(n):
            mn=min(mn,getMin(0,i))
        return mn
        