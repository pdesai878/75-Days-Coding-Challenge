class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def bisect_left(x):
            lo, hi = 0,n
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid][0] < x: lo = mid + 1
                else: hi = mid
            return lo
            
           
        
        @lru_cache(None)
        def getMax(ind):
            if ind>=n:
                return 0
            #exc
            ans=getMax(ind+1)
            #inc
            nxtInd=bisect_left(arr[ind][1])
            ans=max(ans,arr[ind][2]+getMax(nxtInd))
            return ans
            
            
            
        
        arr=list(zip(startTime,endTime,profit))
        arr.sort()
        n=len(arr)
        return getMax(0)
            
       
        