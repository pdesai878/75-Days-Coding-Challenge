class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def getMin(i,j):
            if (i,j)==(row-1,col-1):
                return grid[i][j]
            if i>=row or j>=col:
                return sys.maxsize
            if dp[i][j]!=-1:
                return dp[i][j]
            down=grid[i][j]+getMin(i+1,j)
            right=grid[i][j]+getMin(i,j+1)
            dp[i][j]=min(down,right)
            return dp[i][j]
        
        row=len(grid)
        col=len(grid[0])
        dp=[[-1 for j in range(col)] for i in range(row)]
        return getMin(0,0)
        