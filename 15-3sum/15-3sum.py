class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            el=nums[i]
            left=i+1
            right=n-1
            while left<right:
                s=el+nums[left]+nums[right]
                if s<0:
                    left+=1
                elif s>0:
                    right-=1
                else:
                    res.append([el,nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return res
                