class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(l,r):
            if l<r:
                mid=l+(r-l)//2
                mergeSort(l,mid)
                mergeSort(mid+1,r)
                merge(l,mid+1,r)
                
        def merge(start,mid,end):
            i=start
            j=mid
            temp=[]
            while i<mid and j<=end:
                if arr[i][0]>arr[j][0]:
                    count[arr[i][1]]+=(end-j+1)
                    temp.append(arr[i])
                    i+=1
                else:
                    temp.append(arr[j])
                    j+=1
            
            while i<mid:
                temp.append(arr[i])
                i+=1
            
            while j<=end:
                temp.append(arr[j])
                j+=1
            
            for k in range(start,end+1):
                arr[k]=temp[k-start]
            
        arr=[(el,ind) for ind,el in enumerate(nums)]
        n=len(nums)
        count=[0]*n
        mergeSort(0,n-1)
        return count
        
        