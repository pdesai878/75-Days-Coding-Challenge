class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def getMin(i,j):
            if i>j:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            mn=sys.maxsize
            for k in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]
                cost+=getMin(i,k-1)+getMin(k+1,j)
                mn=min(mn,cost)
            
            dp[i][j]=mn
            return mn
        
        N=len(cuts)
        cuts=[0]+cuts+[n]
        cuts.sort()
        dp=[[-1 for j in range(N+1)] for i in range(N+1)]
        return getMin(1,N)
            