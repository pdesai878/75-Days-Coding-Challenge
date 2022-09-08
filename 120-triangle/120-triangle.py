class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def getMin(ind,i):
            if ind==n-1:
                return triangle[ind][i]
            if ind>=n:
                return sys.maxsize
            if dp[ind][i]!=-1:
                return dp[ind][i]
            op1=triangle[ind][i]+getMin(ind+1,i)
            op2=triangle[ind][i]+getMin(ind+1,i+1)
            dp[ind][i]=min(op1,op2)
            return dp[ind][i]
        
        n=len(triangle)
        dp=[[-1 for j in range(n)] for i in range(n)]
        return getMin(0,0)
            
                
                
            
        