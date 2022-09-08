class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        if n==1:
            return triangle[0][0]
        dp=[[0 for j in range(n)] for i in range(2)]
        for c in range(n):
            dp[(n-1)&1][c]=triangle[n-1][c]
        
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i&1][j]=triangle[i][j]+min(dp[(i+1)&1][j],dp[(i+1)&1][j+1])
           
        return dp[i&1][0]
        
       
            
                
                
            
        