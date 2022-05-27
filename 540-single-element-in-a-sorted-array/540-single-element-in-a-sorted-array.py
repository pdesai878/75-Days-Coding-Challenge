class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        left=0
        right=n-1
        while left<right:
            mid=left+(right-left)//2
            if (mid&1 and nums[mid]==nums[mid-1]) or (mid&1==0 and nums[mid]==nums[mid+1]):
                left=mid+1
            else:
                right=mid
        return nums[left]
            
        
        