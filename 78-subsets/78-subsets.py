class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nsubsets=1<<n
        
        for i in range(nsubsets):
            temp=[]
            for j in range(n):
                if i&1<<j:
                    temp.append(nums[j])
            
            res.append(temp)
                
        return res
        
        