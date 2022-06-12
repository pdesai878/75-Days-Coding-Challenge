class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        i=0
        s=0
        for j in range(n):
            s+=nums[j]
            
            while s*(j-i+1)>=k:
                s-=nums[i]
                i+=1
                
            count+=(j-i+1)
        return count
            
        
                
                
        