class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        res=[]
        for word in l:
            if word:
                res.append(word)
        return " ".join(res[::-1])
            
        
        