#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        l=r=0
        while l<n and r<m:
            if arr1[l]<=arr2[r]:
                
                k-=1
                if k==0:
                    return arr1[l]
                l+=1
            else:
                
                k-=1
                if k==0:
                    return arr2[r]
                r+=1
                    
        while l<n:
            
            k-=1
            if k==0:
                return arr1[l]
            l+=1
        
        while r<m:
            
            k-=1
            if k==0:
                return arr2[r]
            r+=1
        
            
                
    
        
            
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends