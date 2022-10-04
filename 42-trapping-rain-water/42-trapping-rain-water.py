class Solution:
    def trap(self, height: List[int]) -> int:
        """
        the level of water contained above each bar=
        min(ngl,ngr)- height[curr]    
        """
        n=len(height)
        ngl=[height[0]]
        ngr=[height[-1]]
        for i in range(1,n):
            ngl.append(max(ngl[-1],height[i]))
            ngr.append(max(ngr[-1],height[n-i-1]))
        ngr.reverse()
        water=0
        for i in range(n):
            mn=min(ngl[i],ngr[i])-height[i]
            water+=mn
        return water
            
            
        
    
        
            
        