class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def getMax(ind,buy):
            if ind==n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy: 
                profit=max(-prices[ind]+getMax(ind+1,0), getMax(ind+1,1))   
            else:
                profit=max(prices[ind]+getMax(ind+1,1), getMax(ind+1,0))
            dp[ind][buy]=profit
            return dp[ind][buy]
                
  
        n=len(prices)
        dp=[[0 for j in range(2)] for i in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j:
                    dp[i][j]=max(-prices[i]+dp[i+1][0], dp[i+1][1])
                else:
                    dp[i][j]=max(prices[i]+dp[i+1][1], dp[i+1][0])
        
        return dp[0][1]
                    

                    
        

                
        