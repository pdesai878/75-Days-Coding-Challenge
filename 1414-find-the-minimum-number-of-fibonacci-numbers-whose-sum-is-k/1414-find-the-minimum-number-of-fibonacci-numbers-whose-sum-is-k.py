class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def getMin(arr,k):
            count=0
            ind=len(arr)-1
            while k:
                if arr[ind]>k:
                    ind-=1
                else:
                    k-=arr[ind]
                    count+=1
                    
            
            return count

        arr=[]
        prev1=prev2=1
        if k<3:
            arr.extend([1]*k)
        else:
            arr.extend([1]*2)
        for _ in range(2,k+1):
            curr=prev1+prev2
            if curr>k:
                break
            arr.append(curr)
            prev2=prev1
            prev1=curr
        
        return getMin(arr,k)
            
            
            
        