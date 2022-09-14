class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def compare(s1,s2):
            n1=len(s1)
            n2=len(s2)
            if abs(n2-n1)>1 or n1==n2:
                return False
            i=j=0
           
            while j<n2:
                if i<n1 and s1[i]==s2[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            return i==n1 and j==n2
        
        n=len(words)
        words.sort(key=len)
        dp=[1]*n
        mx=1
        for ind in range(1,n):
            s2=words[ind]
            for prev in range(ind):
                s1=words[prev]
                if compare(s1,s2) and dp[ind]<dp[prev]+1:
                    dp[ind]=dp[prev]+1
            mx=max(mx,dp[ind])
        # print(dp)
        return mx
                
                
        