#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        
        def find_dup():
            # arr.sort()
            # for i in range(1,n):
            #     if arr[i]==arr[i-1]:
            #         return arr[i]
            
            for i in range(n):
                ind=abs(arr[i])-1
                if arr[ind]<0:
                    return ind+1
                arr[ind]*=-1
                
            # s={}
            # for el in arr:
            #     if el not in s:
            #         s[el]=1
            #     else:
            #         s[el]+=1
            #         return el
                    
            slow=fast=arr[0]-1
            while True:
                slow=arr[slow]
                fast=arr[arr[fast]]
                if slow==fast:
                    break
            slow=arr[0]-1
            while slow!=fast:
                slow=arr[slow]
                fast=arr[fast]
            return fast
            
        actual_sum=sum(arr)
        expected_sum=n*(n+1)//2
        
        dup=find_dup()
        
        diff=expected_sum-actual_sum
        
        return dup,dup+diff
            
                
    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends