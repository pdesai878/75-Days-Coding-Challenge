#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        
        def find_dup():
            s={}
            for el in arr:
                if el not in s:
                    s[el]=1
                else:
                    s[el]+=1
                    return el
            # slow=fast=arr[0]
            # while True:
            #     slow=arr[slow]
            #     fast=arr[arr[fast]]
            #     if slow==fast:
            #         break
            # slow=arr[0]
            # while slow!=fast:
            #     slow=arr[slow]
            #     fast=arr[fast]
            # return fast
            
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