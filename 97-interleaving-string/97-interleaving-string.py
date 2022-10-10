class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def solve(i,j,k):
            if i==n and j==m:
                return True
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            ans=False
            if i<n and s1[i]==s3[k]:
                ans|= solve(i+1,j,k+1)
            if j<m and s2[j]==s3[k]:
                ans|= solve(i,j+1,k+1)
            dp[i][j][k]=ans
            return ans
        
        n=len(s1)
        m=len(s2)
        l=len(s3)
        if n+m!=l: return False
        dp=[[[-1 for k in range(l+1)] for j in range(m+1) ] for i in range(n+1)]
        return solve(0,0,0)
            
            
        
        
        
        