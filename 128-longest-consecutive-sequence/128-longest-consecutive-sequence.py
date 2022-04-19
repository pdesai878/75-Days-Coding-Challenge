class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        mx=0
        for el in nums:
            if el-1 in s:
                continue
            count=1
            search_el=el+1
            while search_el in s:
                count+=1
                search_el+=1
            mx=max(mx,count)
        return mx
        