class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def get_lcs(i,j,dp):
            if i==0 or j==0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+get_lcs(i-1,j-1,dp)
            else:
                dp[i][j]=max(get_lcs(i-1,j,dp), get_lcs(i,j-1,dp))
            return dp[i][j]
                    
                
        def lcs(s1,s2):
            n=m=len(s1)
            dp=[[-1 for j in range(m+1)] for i in range(n+1)]
            return get_lcs(n,m,dp)
            
        s1=s
        s2=s[::-1]
        return lcs(s1,s2)
            
        