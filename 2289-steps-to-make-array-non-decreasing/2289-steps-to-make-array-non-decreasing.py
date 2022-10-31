class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n=len(nums)
        mx=0
        stack=[]
        for i in range(n-1,-1,-1):
            count=0
            while stack and nums[stack[-1][0]]<nums[i]:
                count=max(count+1,stack.pop()[1])
            mx=max(mx,count)  
            stack.append((i,count))
        return mx
            
        