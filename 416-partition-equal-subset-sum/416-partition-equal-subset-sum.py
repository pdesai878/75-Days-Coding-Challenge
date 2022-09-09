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
            
            if ind==0:
                return True if nums[ind]==s else False
            
            if dp[ind][s]!=-1:
                return dp[ind][s]
            
            #not pick
            not_pick=subsetSum(ind-1,s)
            #pick
            pick=False
            if nums[ind]<=target:
                pick=subsetSum(ind-1,s-nums[ind])
            dp[ind][s]=pick or not_pick
            return dp[ind][s]
        
        sum_=sum(nums)
        if sum_&1:
            return False
        target=sum_//2
        n=len(nums)
        dp=[[-1 for j in range(target+1)]for i in range(n)] 
        return subsetSum(n-1,target)
       
        
            
            
        
        
        