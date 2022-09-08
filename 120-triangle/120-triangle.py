class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        if n==1:
            return triangle[0][0]
        
        prev=triangle[n-1]
    
        for i in range(n-2,-1,-1):
            curr=[0]*n
            for j in range(i,-1,-1):
                curr[j]=triangle[i][j]+min(prev[j],prev[j+1])
            prev=curr
        return curr[0]
        
       
            
                
                
            
        