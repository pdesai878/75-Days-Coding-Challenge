class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1:
            if arr[0]!=1:
                return 1
            return 2
        for ind,el in enumerate(arr):
            if el<=0:
                arr[ind]=n+1
        print(arr)
        for i in range(n):
            ind=abs(arr[i])-1
            if ind>=n:
                continue
            if arr[ind]>0:
                arr[ind]*=-1
           
            
        for ind,el in enumerate(arr):
            if el>0:
                return ind+1
        return n+1
        
                
                
            
            
        