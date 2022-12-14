class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def getMax(ind):
            if ind>=n:
                return 0
            p=nums[ind]+getMax(ind+2)
            np=getMax(ind+1)
            return max(p,np)
        
        n=len(nums)
        return getMax(0)
        