class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=1
        count=0
        for j in range(1,n):
            if nums[j]!=nums[j-1]:
                nums[i]=nums[j]
                i+=1
 
        return i
                    
            