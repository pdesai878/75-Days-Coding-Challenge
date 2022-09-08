class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:        
        row=len(grid)
        col=len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        dp=[[0 for j in range(col)] for i in range(2)]
        
        for i in range(row):
            for j in range(col):
                if i>=0 and j>=0 and grid[i][j]==1:
                    dp[i&1][j]=0
                    continue
                    
                if i==0 and j==0:
                    dp[i&1][j]=1
                    continue
                        
                up=left=0
                
                if i>0: 
                    up = dp[(i-1)&1][j]
                if j>0:
                    left = dp[i&1][j-1]
                    
                dp[i&1][j]=up+left
                
        print(dp)
        return dp[i&1][-1]
                
        
        