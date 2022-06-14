class Solution:
    def reverseWords(self, s: str) -> str:
        temp=""
        n=len(s)
        res=[]
        for i in range(n):
            if s[i]==" ":
                if temp:
                    res.append(temp)
                    temp=""
            else:
                temp+=s[i]
        if temp:
            res.append(temp)
        return " ".join(res[::-1])
                
            
        
            
        
        