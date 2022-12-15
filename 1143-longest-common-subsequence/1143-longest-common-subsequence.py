class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n=len(text1)
        m=len(text2)
        
        dp=[[0 for j in range(m+1)] for i in range(2)]
    
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i&1][j]=1+dp[(i-1)&1][j-1]
                else:
                    dp[i&1][j]=max(dp[(i-1)&1][j],dp[i&1][j-1])
                    
        return dp[i&1][m]
        