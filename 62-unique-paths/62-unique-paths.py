class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        
        dp=[[0 for j in range(n)] for i in range(2)]
        
    
        dp[0][0]=1
        dp[1][0]=1
        for col in range(n):
            dp[0][col]=1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i&1][j]=dp[(i-1)&1][j]+dp[i&1][j-1]
                
        return dp[i&1][j]
       
            
                
            