class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        req=0
        stack=[]
        for ch in s:
            if ch=="(":
                stack.append(ch)
            else:
                if not stack:
                    req+=1
                    
                elif stack[-1]!="(":
                    req+=1
                    
                else:
                    stack.pop()
        req+=len(stack)
        return req
                
        
        