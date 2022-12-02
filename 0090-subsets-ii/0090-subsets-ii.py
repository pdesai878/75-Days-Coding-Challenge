class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        n=len(nums)
        N=1<<n
        
        for i in range(N):
            sub=[]
            for j in range(n):
                if i&(1<<j):
                    sub.append(nums[j])
            res.add(tuple(sorted(sub)))
        return res
                
        