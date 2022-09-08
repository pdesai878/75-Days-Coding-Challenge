class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:        
        row=len(grid)
        col=len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        prev=[0]*col
        
        for i in range(row):
            curr=[0]*col
            for j in range(col):
                if i>=0 and j>=0 and grid[i][j]==1:
                    curr[j]=0
                    continue
                    
                if i==0 and j==0:
                    curr[j]=1
                    continue
                        
                up=left=0
                
                if i>0: 
                    up = prev[j]
                if j>0:
                    left = curr[j-1]
                    
                curr[j]=up+left
            prev=curr
                
       
        return curr[-1]
                
        
        