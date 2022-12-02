class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        def getCombo(target,temp,ind):
            if target==0:
               
                res.append(temp)
                   
                return
            if target<0:
                return
            for i in range(ind,n):
                if i!=ind and candidates[i]==candidates[i-1]:
                    continue
                getCombo(target-candidates[i],temp+[candidates[i]],i+1)
        res=[]
        n=len(candidates)
        candidates.sort()
       
        getCombo(target,[],0)
        return res