class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def getMax(ind,buy,k):
            if k==0 or ind==n:
                return 0  
            if (ind,buy,k) in dp:
                return dp[(ind,buy,k)]
            if buy:
                profit=max(-prices[ind]+getMax(ind+1,0,k),getMax(ind+1,1,k))
            else:
                profit=max(prices[ind]+getMax(ind+1,1,k-1), getMax(ind+1,0,k))
            dp[(ind,buy,k)]=profit
            return profit
        
        n=len(prices)
        dp={}
        return getMax(0,1,2)
            
            
        