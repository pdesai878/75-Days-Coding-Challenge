class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def getTarget(ind,s):
            if ind==n:
                if s==target:
                    return 1
                return 0
            if dp[ind][s]!=-1:
                return dp[ind][s]
            add=getTarget(ind+1,s+(nums[ind]))
            sub=getTarget(ind+1,s-(nums[ind]))
            dp[ind][s]=add+sub
            return dp[ind][s]
        
        n=len(nums)
        totalSum=sum(nums)
        dp=[[-1 for j in range(2*totalSum+1)]for i in range(n+1)]
        return getTarget(0,0)
            
            
        