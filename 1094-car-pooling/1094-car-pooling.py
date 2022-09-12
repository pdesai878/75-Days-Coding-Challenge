class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0]*1001
        for p,pick,drop in trips:
            arr[pick]+=p
            arr[drop]-=p
        
        for el in arr:
            capacity-=el
            if capacity<0:
                return False
        return True
     
            
        
            