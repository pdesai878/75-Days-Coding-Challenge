class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seti=set()
        i=0
        n=len(s)
        mx=1
        for j in range(n):
            while i<n and s[j] in seti:
                seti.remove(s[i])
                i+=1
            seti.add(s[j])
            mx=max(mx,j-i+1)
        return mx
            
                
            
                    
            
        