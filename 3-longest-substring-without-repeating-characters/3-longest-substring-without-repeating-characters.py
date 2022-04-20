class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        mx=1
        n=len(s)
        seti=set()
        i=0
        for j in range(n):
            while s[j] in seti and i<n:
                seti.remove(s[i])
                i+=1
            seti.add(s[j])
            mx=max(mx,j-i+1)
        return mx
            
            
                    
            
        