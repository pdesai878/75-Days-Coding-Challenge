class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        mnBuy=prices[0]
        mxProfit=0
        for el in prices[1:]:
            
            if el-mnBuy>0:
                mxProfit=el-mnBuy
                mx+=mxProfit
            mnBuy=el
        return mx
       
        