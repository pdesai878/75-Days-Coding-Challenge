class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def getCombo(ind,sub,target):
            if target==0:
                res.append(sub)
                return
            
            elif target<0 or ind>=n:
                return
            
            
            getCombo(ind,sub+[candidates[ind]],target-candidates[ind])
            getCombo(ind+1,sub,target)
            
        
        res=[]
        n=len(candidates)
        candidates.sort()
        getCombo(0,[],target)
        return res