class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n=len(arr)
        m=len(pieces)
        pieces.sort(key=lambda x:x[0])
        i=0
        while i<n:
            left=0
            right=m-1
            found=-1
            while left<=right:
                mid=left+(right-left)//2
                if pieces[mid][0]==arr[i]:
                    found=mid
                    for x in pieces[mid]:
                        if x!=arr[i]:
                            return False
                        i+=1
                    break
                elif pieces[mid][0]>arr[i]:
                    right=mid-1
                else:
                    left=mid+1
            if found==-1:
                return False
 
        return True
                    
        
      
        