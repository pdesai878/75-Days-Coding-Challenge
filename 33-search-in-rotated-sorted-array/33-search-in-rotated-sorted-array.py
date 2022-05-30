class Solution:
    def search(self, arr: List[int], target: int) -> int:
        def bs(l,r,key):
            
            while l<=r:
                mid=l+(r-l)//2
                if arr[mid]==key:
                    return mid
                if arr[mid]<key:
                    l=mid+1
                else:
                    r=mid-1
            return -1
        
        def find_pivot():
            l=0
            r=n-1
            pivot=-1
            while l<=r:
                mid=l+(r-l)//2
                if arr[0]<=arr[mid]:
                    pivot=mid
                    l=mid+1
                else:
                    r=mid-1
            return pivot
                    
                    
         
        n=len(arr)
        pivot=find_pivot()
        bs1=bs(0,pivot,target)
        if bs1!=-1:
            return bs1
        return bs(pivot+1,n-1,target)
           
        
            
                
            
                    
                
        