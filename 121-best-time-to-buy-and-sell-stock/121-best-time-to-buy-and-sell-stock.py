class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mnBuy=prices[0]
        mxSell=0
        for el in prices[1:]:
            mxSell=max(mxSell,el-mnBuy)
            mnBuy=min(mnBuy,el)
        return mxSell
        
            