class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def getCost(avg):  
            res=0
            for i in range(n):
                times=abs(nums[i]-avg)
                res+=(times*cost[i])
            return res
        
        n=len(nums)
        l=min(nums)
        r=max(nums)
        while l<r:
            mid=l+(r-l)//2
            lcost=getCost(mid)
            rcost=getCost(mid+1)
            if lcost<rcost:
                r=mid
            else:
                l=mid+1
        return getCost(l)
            
        
        
            
        