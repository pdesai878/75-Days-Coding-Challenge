class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                s=nums[i]+nums[j]
                
                left=j+1
                right=n-1
                
                while left<right:
                    curr=s+nums[left]+nums[right]
                    
                    if curr<target:
                        left+=1
                    elif curr>target:
                        right-=1
                        
                    else:
                        res.add(tuple((nums[i],nums[j],nums[left],nums[right])))
                        while left+1<right and nums[left]==nums[left+1]:
                            left+=1
                        while right-1>left and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
        return res
        
                            
                
                
        