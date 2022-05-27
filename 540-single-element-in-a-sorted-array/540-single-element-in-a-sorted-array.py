class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        
        #boundary checks
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        
        l=0
        r=n-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if (mid&1 and nums[mid]==nums[mid-1]) or (mid&1==0 and nums[mid]==nums[mid+1]):
                l=mid+1
            else:
                r=mid-1
        return -1
        
        