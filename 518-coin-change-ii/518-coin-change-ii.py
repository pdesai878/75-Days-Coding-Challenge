class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def getWays(ind,target):
            if target==0:
                return 1
            if ind==0:
                if target%coins[ind]==0:
                    return 1
                return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            #not take
            nt=getWays(ind-1,target)
            #take
            t=0
            if coins[ind]<=target:
                t=getWays(ind,target-coins[ind])
            dp[ind][target]=t+nt
            return dp[ind][target]
        
        n=len(coins)
        dp=[[-1 for j in range(amount+1)] for i in range(n)]
        return getWays(n-1,amount)
            
            
        