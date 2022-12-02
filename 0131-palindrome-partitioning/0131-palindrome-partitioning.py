class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            return string==string[::-1]
        
        def getPartitions(ind,temp):
            if ind>=n:
                res.append(temp)
                return
            
            for i in range(ind,n):
                substr=s[ind:i+1]
                if isPalindrome(substr):
                    getPartitions(i+1,temp+[substr])
                
        n=len(s)
        res=[]
        getPartitions(0,[])
        return res
        