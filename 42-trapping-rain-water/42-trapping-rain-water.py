class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        water=0
        i=0
        j=n-1
        leftMax=arr[0]
        rightMax=arr[n-1]
        while i<=j:
            if arr[i]<=arr[j]:
                if arr[i]>=leftMax:
                    leftMax=arr[i]
                else:
                    water+=leftMax-arr[i]
                i+=1
            else:
                if arr[j]>=rightMax:
                    rightMax=arr[j]
                else:
                    water+=rightMax-arr[j]
                j-=1
        return water
                
                
            
        
                
        
        