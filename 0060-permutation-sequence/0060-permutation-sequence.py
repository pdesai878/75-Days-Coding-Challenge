class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=1
        numbers=[]
        for i in range(1,n):
            fact*=i
            numbers.append(i)
            
        # given n we find (n-1)!
        numbers.append(n)
        
        # reduce k by 1
        k-=1
        
        ans=""
        while True:
            ind=k//fact
            ans+= str(numbers[ind])
            numbers.pop(ind)
            n=len(numbers)
            if n==0:
                break
            k%=fact
            fact//=n
        return ans
            
            
            
            
            
        
            
            
        
        