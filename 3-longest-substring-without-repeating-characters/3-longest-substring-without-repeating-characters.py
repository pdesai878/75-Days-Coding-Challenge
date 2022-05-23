class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicti={}
        i=mx=0
        for j,el in enumerate(s):
            if el in dicti:
                i=max(i,dicti[el]+1)
            dicti[el]=j
            mx=max(mx,j-i+1)
        return mx
                
            
                    
            
        