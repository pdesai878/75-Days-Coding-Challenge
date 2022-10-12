class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i=0
        n=len(arr)
        
        while i<n:
            
            el=arr[i]
            for p in pieces:
                if p[0]==el:
                    break
            else:
                return False
            
            for x in p:
                if x!=arr[i]:
                    return False
                i+=1
        return True
        