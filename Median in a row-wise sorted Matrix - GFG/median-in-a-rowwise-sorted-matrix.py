#User function Template for python3
import bisect
class Solution:
    def median(self, matrix, r, c):
        def upper_bound(a,x):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if a[mid] > x: hi = mid
                else: lo = mid + 1
            return lo
                    
                    
        
        
        row,col=len(matrix),len(matrix[0])
        if row==1 and col==1:
            return matrix[0][0]
          
        l=0
        r=2000
        
        req=(row*col)//2+1
        
        while l<r:
            mid=l+(r-l)//2
            
            smaller_elements=0
            for row in matrix:
                smaller_elements+=upper_bound(row,mid)
           
            if smaller_elements<req:
                l=mid+1
            else:
                r=mid
        return l
    	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends