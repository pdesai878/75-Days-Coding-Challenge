class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dicti={}
        i=0
        n=len(s)
        mx=1
        for j in range(n):
            if s[j] in dicti:
                i=max(i,dicti[s[j]]+1)
            dicti[s[j]]=j
            mx=max(mx,j-i+1)
            
        return mx
            
                
            
                    
            
        