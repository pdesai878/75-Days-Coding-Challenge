class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_combo(temp,s,ind):
            if s>target:
                return 
            
            if s==target:
                res.append(temp)
                return
                
            for i in range(ind,n):
                get_combo(temp+[candidates[i]],s+candidates[i],i)
        res=[]
        n=len(candidates)
        # candidates.sort()
        get_combo([],0,0)
        return res
                
        