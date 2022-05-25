class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        water=0
        left=[0]*n
        right=[0]*n
        left[0]=arr[0]
        right[n-1]=arr[n-1]
        for i in range(n):
            if i==0:
                continue
            left[i]=max(left[i-1],arr[i])
            right[n-i-1]=max(right[n-i],arr[n-1-i])
       
        for i in range(1,n):
            water+=min(left[i],right[i])-arr[i]
        return water
            
            
        
                
        
        