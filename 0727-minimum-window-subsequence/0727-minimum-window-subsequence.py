class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n=len(s1)
        m=len(s2)
        i=j=0
        ans=""
        mn=sys.maxsize
        while i<n:
            if s1[i]==s2[j]:
                j+=1
                if j==m:
                    end=i+1
                    j-=1
                   
                    while j>=0:
                        if s1[i]==s2[j]:
                            j-=1
                        i-=1
                        
                    j+=1
                    i+=1
                    if end-i<mn:
                        mn=end-i
                        ans=s1[i:end]
                    
            
            i+=1
            
        return ans
         
            
        
         