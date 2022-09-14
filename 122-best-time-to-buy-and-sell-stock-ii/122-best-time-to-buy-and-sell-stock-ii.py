class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        prev=[0]*2
        for i in range(n-1,-1,-1):
            curr=[0]*2
            for j in range(2):
                if j:
                    curr[j]=max(-prices[i]+prev[0], prev[1])
                else:
                    curr[j]=max(prices[i]+prev[1], prev[0])
            prev=curr
        
        return curr[1]
                    

                    
        

                
        