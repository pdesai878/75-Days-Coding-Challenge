class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def getWays(ind):
            if ind==n:
                return 1
            if ind>=n:
                return 0
            return getWays(ind+1)+getWays(ind+2)
        
        return getWays(0)
        