class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(ind):
            if ind==n:
                ans.append(nums[::])
                return
               
            for i in range(ind,n):
                nums[ind],nums[i]=nums[i],nums[ind]
                solve(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]
                            
        ans=[]
        n=len(nums)
        solve(0)
        return ans
                
        
        
        