class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        mx=1
        n=len(s)
        dicti={}
        i=0
        for j in range(n):
            if s[j] in dicti:
                i=max(dicti[s[j]]+1,i)
                dicti[s[j]]=j
            else:
                dicti[s[j]]=j
            mx=max(mx,j-i+1)
        return mx
            
            
                    
            
        