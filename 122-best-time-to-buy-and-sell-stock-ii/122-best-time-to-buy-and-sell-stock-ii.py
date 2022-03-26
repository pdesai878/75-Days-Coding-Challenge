class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def getMaxProfit(ind,prevBuy):
            if ind==len(prices):
                return 0
            mx=0
            #buy now or dont buy now
            if not prevBuy:
                mx=max(-prices[ind]+getMaxProfit(ind+1,True),
                       getMaxProfit(ind+1,prevBuy))
                       
            #sell now or dont sell
            else:
                mx=max(prices[ind]+getMaxProfit(ind+1,False), getMaxProfit(ind+1,prevBuy))
            return mx
                       
        return getMaxProfit(0,False)
                       
            
                
                       
                     
            
            
        