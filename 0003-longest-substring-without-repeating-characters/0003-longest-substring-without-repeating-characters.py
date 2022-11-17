class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dicti={}
        i=0
        n=len(s)
        mx=1
        for j in range(n):
            ch=s[j]
            
            while ch in dicti and i<=j:
                dicti[s[i]]-=1
                if dicti[s[i]]==0:
                    del dicti[s[i]]
                i+=1
           
            mx=max(mx,j-i+1)
            dicti[ch]=1
        return mx
            
        
        
        
        