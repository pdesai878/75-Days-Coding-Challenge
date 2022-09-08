class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        def getWays(i,j):
            if (i,j)==(row-1,col-1):
                return 1
            if i>=row or j>=col:
                return 0
            if grid[i][j]==1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=getWays(i+1,j)+getWays(i,j+1)
            return dp[i][j]
        
        row=len(grid)
        col=len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        dp=[[-1 for j in range(col)] for i in range(row)]
        return getWays(0,0)
        