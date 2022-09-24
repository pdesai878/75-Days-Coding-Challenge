class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        dicti={}
        i=0
        mx=1
        n=len(s)
        for j in range(n):
            if s[j] in dicti:
                dicti[s[j]]+=1
            else:
                dicti[s[j]]=1
            
            while len(dicti)>k and i<n:
                if s[i] in dicti:
                    dicti[s[i]]-=1
                    if dicti[s[i]]==0:
                        del dicti[s[i]]
                i+=1
                
            mx=max(mx,j-i+1)
        return mx
            
        
        