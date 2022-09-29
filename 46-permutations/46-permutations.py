class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def getPermutations(ind): 
            if ind==n:
                res.append(nums[::])
                return
            
            for i in range(ind,n):
                nums[i],nums[ind]=nums[ind],nums[i]
                getPermutations(ind+1)
                nums[i],nums[ind]=nums[ind],nums[i]
                
            
        
        res=[]
        n=len(nums)
        getPermutations(0)
        return res
       