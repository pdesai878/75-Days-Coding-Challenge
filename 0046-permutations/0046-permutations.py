class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def getPermutations(ind,per):
            if ind>=n:
                res.append(per)
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i]=True
                    getPermutations(ind+1,per+[nums[i]])
                    visited[i]=False
          
        n=len(nums)
        res=[]
        visited=[False for _ in range(n)]
        getPermutations(0,[])
        return res
        
        