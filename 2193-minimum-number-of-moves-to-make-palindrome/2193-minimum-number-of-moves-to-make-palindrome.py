class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s=list(s)
        n=len(s)
        left=0
        right=n-1
        ans=0
        while left<=right:
            l=left
            r=right
            if s[l]!=s[r]:
                while s[r]!=s[l]:
                    r-=1
                
                if l==r:
                    s[r],s[r+1]=s[r+1],s[r]
                    ans+=1
                    continue
                
                while r<right:
                    s[r],s[r+1]=s[r+1],s[r]
                    ans+=1
                    r+=1
            left+=1
            right-=1
        return ans
                    
                    
            
                
        
            
                
        