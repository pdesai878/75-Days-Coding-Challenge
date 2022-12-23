class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def getMax(ind,buy):
            if ind>=n:
                return 0
            if not buy:
                mx=max(-prices[ind]+getMax(ind+1,True),getMax(ind+1,False))
            else:
                mx=max(prices[ind]+getMax(ind+2,False), getMax(ind+1,True))
            
            return mx
        
        n=len(prices)
        return getMax(0,False)
        