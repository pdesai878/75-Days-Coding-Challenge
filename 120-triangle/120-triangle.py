class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[0 for j in range(n)] for i in range(n)]
        for c in range(n):
            dp[n-1][c]=triangle[n-1][c]
        
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j]=triangle[i][j]+min(dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]
        
       
            
                
                
            
        