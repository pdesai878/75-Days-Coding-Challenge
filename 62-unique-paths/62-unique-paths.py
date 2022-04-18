class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def get_paths(i,j):
            if (i,j)==(m-1,n-1):
                return 1
                
            if i>=m or j>=n:
                return 0
            
            return get_paths(i+1,j)+get_paths(i,j+1)
        
        return get_paths(0,0)
       
            
                
            