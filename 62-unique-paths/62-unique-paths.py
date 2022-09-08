class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def getPaths(i,j):
            if (i,j)==(m-1,n-1):
                return 1
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=getPaths(i+1,j)+getPaths(i,j+1)
            return dp[i][j]
        dp=[[-1 for j in range(n)] for i in range(m)]
        return getPaths(0,0)
        
            
                
            