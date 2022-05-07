class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def gen_subsets(res,ind):
            s.add(tuple(res))
            for i in range(ind,n):
                gen_subsets(res+[nums[i]],i+1)
            
            
        s=set()
        nums.sort()
        n=len(nums)
        gen_subsets([],0)
        return s
            