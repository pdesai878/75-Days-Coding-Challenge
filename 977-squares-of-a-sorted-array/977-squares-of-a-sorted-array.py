class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:    
        """
        intuition: el to be present at the end of the resultant array would be either the square of the first no or the last.
        we will keep two pointers, one pointing at index 0 and other at index n-1. And pushing the larger el at the end of res arr.
        
        TC: O(n)
        SC: O(n)
        
        """
        n=len(nums)
        res=[0]*n
        left,right=0,n-1
        
        for i in range(n-1,-1,-1):
            if abs(nums[left])<abs(nums[right]):
                res[i]=nums[right]**2
                right-=1
            else:
                res[i]=nums[left]**2
                left+=1
        return res