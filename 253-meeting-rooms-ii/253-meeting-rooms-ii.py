class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res=[]
        for st,en in intervals:
            res.append((st,1))
            res.append((en,-1))
        mx=1
        curr=0
        for time,val in sorted(res):
            curr+=val
            mx=max(mx,curr)
        return mx