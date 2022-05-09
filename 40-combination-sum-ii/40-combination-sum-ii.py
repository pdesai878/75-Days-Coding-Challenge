class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_combo(temp,s,ind):
            if s==target:
                res.add(tuple(temp))
                return
            
            if s>target or ind>=n:
                return 
                
            for i in range(ind,n):
                if i!=ind and candidates[i]==candidates[i-1]:
                    continue
                get_combo(temp+[candidates[i]],s+candidates[i],i+1)
                
            
        res=set()
        n=len(candidates)
        candidates.sort()
        get_combo([],0,0)
        return res
        