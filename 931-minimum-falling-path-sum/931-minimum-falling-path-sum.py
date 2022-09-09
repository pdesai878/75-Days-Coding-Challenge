class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        if n==1:
            return matrix[0][0]
        mn=sys.maxsize
        prev=matrix[-1]
        
        for i in range(n-2,-1,-1):
            curr=[0]*n
            for j in range(n):
                if j==0:
                    curr[j]=matrix[i][j]+min(prev[j],prev[j+1])
                elif j==n-1:
                    curr[j]=matrix[i][j]+min(prev[j],prev[j-1])
                else:
                    curr[j]=matrix[i][j]+min(prev[j],prev[j-1],prev[j+1])
            prev=curr
                    
    
        return min(curr)
        
        