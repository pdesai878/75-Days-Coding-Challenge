class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def getSubsets(ind,sub):
            res.append(sub)
            
            for i in range(ind,n):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                getSubsets(i+1,sub+[nums[i]]) 
        
        res=[]
        n=len(nums)
        nums.sort()
        getSubsets(0,[])
        return res
        
                
        