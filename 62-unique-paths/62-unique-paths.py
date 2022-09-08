class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        #dp initialisation
        dp=[[0 for j in range(n)] for i in range(m)]
        for col in range(n):
            dp[0][col]=1
        for row in range(m):
            dp[row][0]=1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
        
        
            
                
            