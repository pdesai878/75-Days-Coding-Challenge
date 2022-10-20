class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prod=1
        mx=-sys.maxsize
        for i in range(n):
            prod*=nums[i]
            mx=max(mx,prod)
            if prod==0:
                prod=1
            
        prod=1   
        for i in range(n-1,-1,-1):
            prod*=nums[i]
            mx=max(mx,prod)
            if prod==0:
                prod=1
        return mx