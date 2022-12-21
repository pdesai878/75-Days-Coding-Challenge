class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        prev=0
        res=0
        for ind,el in enumerate(nums):
            if el==0:
                if ind>0:
                    if nums[ind-1]==0:
                        res+=(prev)+1
                        prev+=1
                        continue
               
                res+=1
                prev=1
            else:
                prev=0
                 
        return res
                    
                    
                
        