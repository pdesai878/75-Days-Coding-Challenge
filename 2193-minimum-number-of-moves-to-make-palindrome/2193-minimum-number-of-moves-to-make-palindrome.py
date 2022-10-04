class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n=len(s)
        s=list(s)
        left=0
        right=n-1
        swaps=0
        while left<=right:
            l=left
            r=right
            if s[l]!=s[r]:
                while s[r]!=s[l]:
                    r-=1
                if l==r:
                    s[l],s[l+1]=s[l+1],s[l]
                    swaps+=1
                    continue
                
                while r<right:
                    s[r],s[r+1]=s[r+1],s[r]
                    swaps+=1
                    r+=1
            left+=1
            right-=1
        return swaps
                    
       
                
                
        