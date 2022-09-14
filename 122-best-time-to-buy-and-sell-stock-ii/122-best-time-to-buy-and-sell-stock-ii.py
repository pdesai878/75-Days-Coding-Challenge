class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for j in range(2)] for i in range(2)]
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j:
                    dp[i&1][j]=max(-prices[i]+dp[(i+1)&1][0], dp[(i+1)&1][1])
                else:
                    dp[i&1][j]=max(prices[i]+dp[(i+1)&1][1], dp[(i+1)&1][0])
        
        return dp[i&1][1]
                    

                    
        

                
        