class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap=[]
        for p,pick,drop in trips:
            heapq.heappush(heap,(pick,p))
            heapq.heappush(heap,(drop,-p))
        onboard=0
        while heap:
            onboard+=heapq.heappop(heap)[1]
            if onboard>capacity:
                return False
        return True
            
        
            