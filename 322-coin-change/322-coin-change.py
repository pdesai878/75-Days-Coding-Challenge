class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def getMinCoins(ind,amount):
            if amount==0:
                return 0
            if amount<0:
                return sys.maxsize
            if ind<0:
                return sys.maxsize
            #not pick
            op1=getMinCoins(ind-1,amount)
            op2=sys.maxsize
            if coins[ind]<=amount:
                op2=min(1+getMinCoins(ind,amount-coins[ind]),getMinCoins(ind-1,amount))
            return min(op1,op2)

        
        n=len(coins)
        res=getMinCoins(n-1,amount)
        return res if res!=sys.maxsize else -1
            
        