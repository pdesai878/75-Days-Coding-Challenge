class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        def reverse(i,j):
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
    
        
        n=len(arr)
        left=right=None
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                left=i
                break
    
        if left is None:
            return arr.sort()
        
        for j in range(n-1,-1,-1):
            print(arr[j])
            if arr[j]>arr[left]:
                right=j
                break
        print(right)
        arr[left],arr[right]=arr[right],arr[left]
        
        reverse(left+1,n-1)
        
        return arr
        
       