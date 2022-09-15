class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]:
            return -1
        n=len(grid)
        q=deque()
        q.append((0,0,1))
        grid[0][0]=1
        while q:
            i,j,steps=q.popleft()
            if (i,j)==(n-1,n-1):
                return steps
            for x,y in [[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j],[i+1,j-1],[i,j-1],[i-1,j-1]]:
                if 0<=x<n and 0<=y<n and grid[x][y]==0:
                    q.append((x,y,steps+1))
                    grid[x][y]=1
        return -1
        
        
        