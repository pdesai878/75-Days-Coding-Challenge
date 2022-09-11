class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        s,e=list(map(list,zip(*intervals)))
        
        s.sort()
        e.sort()
        
        n=len(intervals)
        
        start=0
        end=0
        mx=1
        rooms=0
        while start<n and end<n:
            if s[start]<=e[end]:
                rooms+=1
                start+=1
            else:
                rooms-=1
                end+=1
            mx=max(mx,rooms)
        return mx
        