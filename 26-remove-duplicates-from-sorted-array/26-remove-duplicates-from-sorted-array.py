class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        count=0
        for j in range(n):
            if j>0:
                if nums[j]!=nums[j-1]:
                    nums[i]=nums[j]
                    j+=1
                    i+=1
            else:
                i+=1
        
        return i
                    
            