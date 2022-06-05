class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=1
        prev=0
        n=len(nums)
        for i in range(n):
            if nums[i]-nums[prev]<=k:
                continue
            else:
                count+=1
                prev=i
        return count
            
        