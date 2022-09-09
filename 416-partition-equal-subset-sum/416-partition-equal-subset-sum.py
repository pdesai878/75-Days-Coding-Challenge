class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # s1=s2
        # s1+s2=sum
        # s1-s2=0
        # 2s1=sum
        # s1=sum//2
        # if s1 exists, then partition possible
        
        def subsetSum(ind,s):
            if s==0:
                return True
            
            if s<0 or ind<=0:
                return False
            
            if dp[ind][s]!=-1:
                return dp[ind][s]
            #pick
            pick=not_pick=False
            if nums[ind-1]<=target:
                pick=subsetSum(ind-1,s-nums[ind-1]) or subsetSum(ind-1,s)
            #not pick
            else:
                not_pick=subsetSum(ind-1,s)
            dp[ind][s]=pick or not_pick
            return dp[ind][s]
        
        sum_=sum(nums)
        if sum_&1:
            return False
        target=sum_//2
        n=len(nums)
        dp=[[-1 for j in range(target+1)]for i in range(n+1)] 
        return subsetSum(n,target)
       
        
            
            
        
        
        