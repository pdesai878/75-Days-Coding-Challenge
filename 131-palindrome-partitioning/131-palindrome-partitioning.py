class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            i=0
            j=len(string)-1
            while i<=j:
                if string[i]!=string[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def solve(ind,temp):
            if ind==n:
                res.append(temp)
                return
            for i in range(ind,n):
                if isPalindrome(s[ind:i+1]):
                    solve(i+1,temp+[s[ind:i+1]])
                    
        n=len(s)
        res=[]
        solve(0,[])
        return res
                
                
            
        