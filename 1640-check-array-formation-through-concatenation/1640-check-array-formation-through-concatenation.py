class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dicti={p[0]:p for p in pieces}
        i=0
        n=len(arr)
        while i<n:
            if arr[i] in dicti:
                for x in dicti[arr[i]]:
                    if x!=arr[i]:
                        return False
                    i+=1
            else:
                return False
        return True
    
                    
        
      
        