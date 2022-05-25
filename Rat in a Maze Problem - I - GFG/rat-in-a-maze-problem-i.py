#User function Template for python3

class Solution:
    def findPath(self, m, n):
        def solve(i,j,string):
            if (i,j)==(n-1,n-1):
                res.append(string)
                return
            #down
            if 0<=i+1<n and 0<=j<n and not visited[i+1][j] and m[i+1][j]==1:
                visited[i+1][j]=True
                solve(i+1,j,string+"D")
                visited[i+1][j]=False
            
            #left
            if 0<=i<n and 0<=j-1<n and not visited[i][j-1] and m[i][j-1]==1:
                visited[i][j-1]=True
                solve(i,j-1,string+"L")
                visited[i][j-1]=False
                
            #right   
            if 0<=i<n and 0<=j+1<n and not visited[i][j+1] and m[i][j+1]==1:
                visited[i][j+1]=True
                solve(i,j+1,string+"R")
                visited[i][j+1]=False
            
            #up
            if 0<=i-1<n and 0<=j<n and not visited[i-1][j] and m[i-1][j]==1:
                visited[i-1][j]=True
                solve(i-1,j,string+"U")
                visited[i-1][j]=False
            
        visited=[[False for col in range(n)] for row in range(n)]
        if m[0][0]!=1:
            return []
        res=[]
        visited[0][0]=True
        solve(0,0,"")
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends