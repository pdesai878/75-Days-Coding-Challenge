class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def getPermutations(ind):
            if ind==n:
                res.append(nums[::])
                return 
            
            for i in range(ind,n):
                nums[ind],nums[i]=nums[i],nums[ind]
                getPermutations(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]
                
          
        n=len(nums)
        res=[]
        getPermutations(0)
        return res
        
        