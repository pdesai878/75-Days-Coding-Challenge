class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n=len(arr)
        l=0
        r=n-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]==target:
                return mid
            if arr[mid]>=arr[l]:
                if target>=arr[l] and target<arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if target<=arr[r] and target>arr[mid]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
                
        
        
           
        
            
                
            
                    
                
        