class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def getMin(i,j):   
            if i>j:
                return 0
            mn=sys.maxsize
            for k in range(i,j+1):
                curr_cost=cuts[j+1]-cuts[i-1]
                mn=min(mn,curr_cost+getMin(i,k-1)+getMin(k+1,j))
            
            return mn
        
        N=len(cuts)
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        return getMin(1,N)
        