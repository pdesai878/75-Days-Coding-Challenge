class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s=set()
        N=len(nums)
        n=1<<N
        for i in range(n):
            temp=[]
            for j in range(N):
                if i & (1<<j):
                    temp.append(nums[j])
            s.add(tuple(sorted(temp)))
        return s