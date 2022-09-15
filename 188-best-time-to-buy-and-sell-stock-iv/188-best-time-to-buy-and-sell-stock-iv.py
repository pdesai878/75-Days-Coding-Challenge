class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def getMax(ind,buy,k):
            if ind==n or k==0:
                return 0
            if dp[ind][buy][k]!=-1:
                return dp[ind][buy][k]
            if buy:
                profit=max(-prices[ind]+getMax(ind+1,0,k),getMax(ind+1,1,k))
            else:
                profit=max(prices[ind]+getMax(ind+1,1,k-1), getMax(ind+1,0,k))
            dp[ind][buy][k]=profit
            return profit
        n=len(prices)
        dp=[[[-1 for k_ in range(k+1)]for j in range(2)] for i in range(n)]
        return getMax(0,1,k)
        