class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        curr=0
        for el in nums:
            if el==0:
                curr+=1
            else:
                curr=0
            res+=curr
                     
        return res
                    
                    
                
        