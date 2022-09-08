class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:    
        row=len(grid)
        col=len(grid[0])
        prev=list(accumulate(grid[0]))
        for i in range(row):
            curr=[0]*col
            for j in range(col):
                if i==0 and j==0:
                    curr[j]=grid[i][j]
                    continue
                    
                up=left=sys.maxsize
                
                if i>0:
                    up=prev[j]+grid[i][j]
                    
                if j>0:
                    left=curr[j-1]+grid[i][j]
                    
                curr[j]=min(up,left)
            prev=curr
            
        return curr[-1]
                    
                    
                  
                  
        