class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def solve(ind):
            if ind==n:
                return True
            if dp[ind]!=-1:
                return dp[ind]
            
            dp[ind]=False
            for i in range(ind,n):
                if s[ind:i+1] in wordDict:
                    if solve(i+1):
                        dp[ind]=True
                        break
            return dp[ind]
                    
        n=len(s)
        dp=[-1 for i in range(n)]
        return solve(0)
                    
        
        