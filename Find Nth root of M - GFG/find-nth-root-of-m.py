#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
	    if m==1 or m==0:
	        return 1
	    if n==1:
	        return m
		l=1
		r=m//n
		while l<=r:
		    mid=l+(r-l)//2
		    sq=mid**n
		    if sq==m:
		        return mid
		    if sq<m:
		        l=mid+1
		    else:
		        r=mid-1
        return -1
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends