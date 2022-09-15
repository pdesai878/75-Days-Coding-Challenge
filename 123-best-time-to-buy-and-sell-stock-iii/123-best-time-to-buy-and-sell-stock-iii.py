class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0 for k in range(3)] for j in range(2)] for i in range(n+1)]
        
        for i in range(n-1,-1,-1):
            for j in range(2):
                for k in range(1,3):
                    if j:
                        dp[i][j][k]=max(-prices[i]+dp[i+1][0][k], dp[i+1][1][k])
                      
                    else:
                                        dp[i][j][k]=max(prices[i]+dp[i+1][1][k-1], dp[i+1][0][k])
                        
        return dp[0][1][2]
            
            
        