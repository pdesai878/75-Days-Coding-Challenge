class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap=[]
        intervals.sort()
        for st,en in intervals:
            if heap and heap[0]<st:
                heapq.heappop(heap)
            heapq.heappush(heap,en)
        return len(heap)
        