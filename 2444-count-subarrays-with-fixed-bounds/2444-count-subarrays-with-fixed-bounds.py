class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def withinB(no):
            return minK<=no<=maxK
        
        subarrs=0
        mnLatest=mxLatest=-1
        n=len(nums)
        i=0
        lastfault=-1
        for j in range(n):
            el=nums[j]
            if not withinB(el):
                lastfault=j
                i=j+1
                mnLatest=mxLates=-1
                continue
            if el==minK:
                mnLatest=j
            if el==maxK:
                mxLatest=j
            subarrs+=max(0,min(mnLatest,mxLatest)-lastfault)
          
               
            
                
        return subarrs
                
        