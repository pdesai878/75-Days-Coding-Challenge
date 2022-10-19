class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        l=r=1
        res[0]=1
        for i in range(1,n):
            res[i]=nums[i-1]*res[i-1]
     
        for i in reversed(range(n)):
            res[i]*=r
            r*=nums[i]
          
    
        return res
        