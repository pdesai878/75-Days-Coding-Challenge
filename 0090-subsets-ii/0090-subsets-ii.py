class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def getSubSum(ind,s):
            if ind>=n:
                sub=tuple(sorted(s))
                if sub not in res:
                    res.add(sub)
                return
            
            getSubSum(ind+1,s+[nums[ind]])
            getSubSum(ind+1,s)
            
        res=set()
        n=len(nums)
        getSubSum(0,[])
        return list(res)
            
        
        