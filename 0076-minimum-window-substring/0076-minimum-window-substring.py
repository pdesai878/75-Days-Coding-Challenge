class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        mn=n+1
        dicti=Counter(t)
        count=len(dicti)
        ans=""
        i=0
        for j in range(n):
            if s[j] in dicti:
                dicti[s[j]]-=1
                if dicti[s[j]]==0:
                    count-=1
            
            if count==0:
                while i<n and not count:
                    if j-i+1<mn:
                        mn=j-i+1
                        ans=s[i:j+1]
                    if s[i] in dicti:
                        dicti[s[i]]+=1
                        if dicti[s[i]]==1:
                            count+=1
                    i+=1
        return ans
                    
            
        