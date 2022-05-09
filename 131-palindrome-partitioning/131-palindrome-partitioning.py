class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(i,j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def get_partitions(temp,ind):
            if ind==n:
                res.append(temp)
                return
            
            for i in range(ind,n):
                if isPalindrome(ind,i):
                    get_partitions(temp+[s[ind:i+1]],i+1)
                    
        res=[]
        n=len(s)
        get_partitions([],0)
        return res
                
                
            
        