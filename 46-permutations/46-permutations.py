class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def getPermutations(ind,temp): 
            if len(temp)==n:
                res.append(temp[::])
                return
               
            for i in range(n):
                if i not in visited:
                    visited.add(i) 
                    getPermutations(i,temp+[nums[i]])
                    visited.remove(i)
        
        res=[]
        n=len(nums)
        visited=set()
        getPermutations(0,[])
        return res
       