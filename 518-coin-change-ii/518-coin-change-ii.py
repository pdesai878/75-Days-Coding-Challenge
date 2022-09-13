class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # def getWays(ind,target):
        #     if target==0:
        #         return 1
        #     if ind==0:
        #         if target%coins[ind]==0:
        #             return 1
        #         return 0
        #     if dp[ind][target]!=-1:
        #         return dp[ind][target]
        #     #not take
        #     nt=getWays(ind-1,target)
        #     #take
        #     t=0
        #     if coins[ind]<=target:
        #         t=getWays(ind,target-coins[ind])
        #     dp[ind][target]=t+nt
        #     return dp[ind][target]
        
        n=len(coins)
        dp=[[0 for j in range(amount+1)] for i in range(n)]
        for r in range(n):
            dp[r][0]=1
        for c in range(amount+1):
            if c%coins[0]==0:
                dp[0][c]=1
        
        for i in range(1,n):
            for j in range(1,amount+1):
                if coins[i]<=j:
                    dp[i][j]=dp[i][j-coins[i]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
                    
                
        
            
            
        