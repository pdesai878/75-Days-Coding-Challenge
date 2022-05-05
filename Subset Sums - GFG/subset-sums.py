#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    def get_sum(s,ind):
	        if ind>=N:
	            res.append(s)
	            return
	        
	        get_sum(s+arr[ind],ind+1)
	        get_sum(s,ind+1)
	        
	            
	    res=[]
	    get_sum(0,0)
	    return res
	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends