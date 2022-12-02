class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def getCombo(ind,sub,target):
            if target==0:
                res.append(sub)
                return
            elif target<0 or ind>=n:
                return
            
            for i in range(ind,n):
                getCombo(i,sub+[candidates[i]],target-candidates[i])
        
        res=[]
        n=len(candidates)
        candidates.sort()
        getCombo(0,[],target)
        return res