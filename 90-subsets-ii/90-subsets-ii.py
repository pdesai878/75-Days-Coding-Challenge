class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def gen_subsets(res,ind):
            s.append(res)
            for i in range(ind,n):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                gen_subsets(res+[nums[i]],i+1)
                
        s=[]
        nums.sort()
        n=len(nums)
        gen_subsets([],0)
        return s
            