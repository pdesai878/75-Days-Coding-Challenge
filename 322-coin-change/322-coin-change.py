class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def getMinCoins(ind,amount):
            if ind==0:
                if amount%coins[ind]==0:
                    return amount//coins[ind]
                return sys.maxsize
            
            if dp[ind][amount]!=-1:
                return dp[ind][amount]
            #not pick
            op1=getMinCoins(ind-1,amount)
            #pick
            op2=sys.maxsize
            if coins[ind]<=amount:
                op2=1+getMinCoins(ind,amount-coins[ind])
            dp[ind][amount]=min(op1,op2)
            return dp[ind][amount]
  
        n=len(coins)
        dp=[[-1 for j in range(amount+1)] for i in range(n)]
        res=getMinCoins(n-1,amount)
        return res if res!=sys.maxsize else -1
            
        