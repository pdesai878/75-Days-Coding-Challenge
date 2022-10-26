class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def check(i,j):
            if i<0 and j<0:
                return True
            
            if j<0 and i>=0:
                return False
            
            if i<0 and j>=0:
                
                for ind in range(j+1):
                    if p[ind]!="*":
                        return False
               
                return True
            
            #match case
            if s[i]==p[j] or p[j]=="?":
                return check(i-1,j-1)
            #* match
            if p[j]=="*":
                return check(i-1,j) or check(i,j-1)
            return False
        return check(len(s)-1,len(p)-1)
        