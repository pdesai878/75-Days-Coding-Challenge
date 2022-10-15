class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def getMin(ind,prev_char,prev,k):
            if k<0:
                return sys.maxsize
            if ind==n:
                return 0
            delete=getMin(ind+1,prev_char,prev,k-1)
            if s[ind]==prev_char:
                keep=getMin(ind+1,prev_char,prev+1,k)
                if prev in [1,9,99]:
                    keep+=1
            else:
                keep=1+getMin(ind+1,s[ind],1,k)
            return min(keep,delete)
        
        n=len(s)
        return getMin(0,"",0,k)
        
            
       
                
                
                
            
        