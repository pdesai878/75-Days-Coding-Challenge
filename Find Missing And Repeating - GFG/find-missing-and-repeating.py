#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        s={}
        for el in arr:
            if el not in s:
                s[el]=1
            else:
                s[el]+=1
        # print(s)
        for i in range(1,n+1):
            if i not in s:
                missing=i
            elif i in s and s[i]>1:
                dup=i
        return dup,missing
            
                
    
        

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