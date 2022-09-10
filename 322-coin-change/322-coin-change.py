class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[sys.maxsize for j in range(amount+1)] for i in range(n)]
        
        prev=[sys.maxsize for j in range(amount+1)]
        for c in range(1,amount+1):
            if c%coins[0]==0:
                prev[c]=c//coins[0]
        prev[0]=0      
        for i in range(n):
            curr=[sys.maxsize for j in range(amount+1)]
            curr[0]=0
            for j in range(1,amount+1):
                if coins[i]<=j:
                    curr[j]=min(1+curr[j-coins[i]], prev[j])
                else:
                    curr[j]=prev[j]
            prev=curr
        return curr[-1] if curr[-1]!=sys.maxsize else -1
                
            
        
            
        