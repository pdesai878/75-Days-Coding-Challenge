class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n=len(stockPrices)
        if n<2:
            return 0
        stockPrices.sort()
        count=1
        for i in range(2,n):
            x1,y1=stockPrices[i]
            x2,y2=stockPrices[i-1]
            x3,y3=stockPrices[i-2]
            
            diff1 = (y3-y2) * (x2-x1)
            diff2 = (y2-y1) * (x3-x2)
            
            if diff1!=diff2:
                count+=1
                
        return count
            
            
        