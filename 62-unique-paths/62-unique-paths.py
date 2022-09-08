class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        #edge case
        if m==1 or n==1:
            return 1
        #dp initialisation
        prev=[1]*n
        
        for i in range(m):
            curr=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    curr[j]=1
                    continue
                up=left=0
                if i>0:
                    up=prev[j]
                if j>0:
                    left=curr[j-1]
                curr[j]=up+left
                    
            prev=curr
            
        return curr[-1]
        
        
            
                
            