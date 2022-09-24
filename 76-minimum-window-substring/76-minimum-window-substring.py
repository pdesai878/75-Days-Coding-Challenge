class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        dicti=Counter(t)
        ans=""
        count=len(dicti)
        i=0
        n=len(s)
        mn=n+1
        for j in range(n):
            el=s[j]
            if el in dicti:
                dicti[el]-=1
                if dicti[el]==0:
                    count-=1
                    
            if count==0:
                while count==0 and i<n:
                    if j-i+1<mn:
                        mn=j-i+1
                        ans=s[i:j+1]
                    if s[i] in dicti:
                        dicti[s[i]]+=1
                        if dicti[s[i]]==1:
                            count+=1
                    i+=1
        return ans
            
                
            
        