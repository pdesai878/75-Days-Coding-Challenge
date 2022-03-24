class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZero=0
        n=len(nums)
        
        for ind,el in enumerate(nums):
            if el!=0:
                nums[lastNonZero]=el
                lastNonZero+=1
                
        for ind in range(lastNonZero,n):
            nums[ind]=0
        return nums
                                            
            
        
        