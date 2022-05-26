class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def solve(ind):
            if ind==n:
                return True
            for i in range(ind,n):
                if s[ind:i+1] in wordDict:
                    if solve(i+1):
                        return True
            return False
                    
        n=len(s)
        return solve(0)
                    
        
        