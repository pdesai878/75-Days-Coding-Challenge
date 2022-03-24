class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZero=0
        n=len(nums)
        
        for ind,el in enumerate(nums):
            if el!=0:
                nums[lastNonZero],nums[ind]=nums[ind],nums[lastNonZero]
                lastNonZero+=1
        return nums
                
                           
            
        
        