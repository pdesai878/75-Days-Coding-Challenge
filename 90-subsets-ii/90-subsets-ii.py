class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def gen_subsets(res,ind):
            if ind>=n:
                s.add(tuple(res))
                return
            gen_subsets(res+[nums[ind]],ind+1)
            gen_subsets(res,ind+1)
            
        s=set()
        nums.sort()
        n=len(nums)
        gen_subsets([],0)
        return s
            