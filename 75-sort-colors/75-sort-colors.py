class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #one pass approach
        n=len(nums)
        left,mid,right=0,0,n-1

        """
        logic to be implemented is: all elements towards left of left pointer will contain all 0s AND all elements towards right of right pointer will contain all 2s. 
        """
        while mid<=right:
                if nums[mid]==0:
                    nums[left],nums[mid]=nums[mid],nums[left]
                    left+=1
                    mid+=1
                elif nums[mid]==1:
                    mid+=1
                elif nums[mid]==2:
                    nums[right],nums[mid]=nums[mid],nums[right]
                    right-=1
        return nums
