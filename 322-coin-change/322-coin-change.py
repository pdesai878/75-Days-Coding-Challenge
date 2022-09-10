class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[sys.maxsize for j in range(amount+1)] for i in range(n)]
        
        for c in range(1,amount+1):
            if c%coins[0]==0:
                dp[0][c]=c//coins[0]
                
        for i in range(n):
            for j in range(amount+1):
                if j==0:
                    dp[i][j]=0
                    continue
                if coins[i]<=j:
                    dp[i][j]=min(1+dp[i][j-coins[i]], dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1] if dp[-1][-1]!=sys.maxsize else -1
                
            
        
            
        