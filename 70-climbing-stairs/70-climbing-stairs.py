class Solution:
    def climbStairs(self, n: int) -> int:
        def getWays(ind):
            if ind==0:
                return 1
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=getWays(ind-1)+getWays(ind-2)
            return dp[ind]
        
        dp=[-1 for steps in range(n+1)]
        return getWays(n)
        