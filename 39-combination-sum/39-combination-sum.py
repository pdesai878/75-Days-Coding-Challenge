class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_combo(temp,s,ind):
            if s>target or ind>=n:
                return 
            
            if s==target:
                res.append(temp)
                return
                
            get_combo(temp,s,ind+1)
            get_combo(temp+[candidates[ind]],s+candidates[ind],ind)
        res=[]
        n=len(candidates)
        get_combo([],0,0)
        return res
                
        