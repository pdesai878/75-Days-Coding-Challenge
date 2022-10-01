class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n=len(arr)
        l=0
        r=n-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]==target:
                return mid
            #check if left half is sorted
            if arr[l]<=arr[mid]:
                #check if target lies in the sorted left half
                if arr[l]<=target<arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            #check if right half is sorted
            else:
                #check if target lies in right half
                if arr[mid]<=target<=arr[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
        
                
                    
                
                
       
        