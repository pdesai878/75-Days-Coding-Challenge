class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        i=0
        n=len(s)
        dicti={}
        mx=1
        for j in range(n):
            if s[j] not in dicti:
                dicti[s[j]]=1
            else:
                dicti[s[j]]+=1
            
            while len(dicti)>k:
                if s[i] in dicti:
                    dicti[s[i]]-=1
                    if dicti[s[i]]==0:
                        del dicti[s[i]]
                    i+=1
            mx=max(mx,j-i+1)
        return mx
                
            
        