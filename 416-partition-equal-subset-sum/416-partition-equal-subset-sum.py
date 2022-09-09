class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # s1=s2
        # s1+s2=sum
        # s1-s2=0
        # 2s1=sum
        # s1=sum//2
        # if s1 exists, then partition possible
     
        sum_=sum(nums)
        if sum_&1:
            return False
        target=sum_//2
        n=len(nums)
        if n==1:
            return nums[0]==target
        prev=[False for j in range(target+1)] 
        prev[0]=True
        for i in range(1,n):
            curr=[False for j in range(target+1)] 
            curr[0]=True
            for j in range(1,target+1):
                if nums[i]<=j:
                    curr[j]=prev[j-nums[i]] or prev[j]
                else:
                    curr[j]=prev[j]
            prev=curr
        return curr[-1]
                
                
       
       
        
            
            
        
        
        