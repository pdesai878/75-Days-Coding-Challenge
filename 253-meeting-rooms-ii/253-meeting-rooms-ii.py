class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap=[]
        heapq.heappush(heap,(intervals[0][1],intervals[0][0]))
        for st,en in intervals[1:]:
            prev_end,prev_st=heapq.heappop(heap)
            if st<prev_end:
                heapq.heappush(heap,(prev_end,prev_st))
            heapq.heappush(heap,(en,st))
        return len(heap)
            
        
       
                
                
                
            
            
        
        