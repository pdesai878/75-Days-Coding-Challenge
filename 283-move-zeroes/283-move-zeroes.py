class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        r=1
        n=len(nums)
        if n==1:
            return nums
        while True:
            while l<n and r<n and nums[l]==0:
                nums[l],nums[r]=nums[r],nums[l]
                r+=1
            l+=1
            if l==r:
                r+=1
            if l==n-1:
                break
        
        return nums
            
            
        
        