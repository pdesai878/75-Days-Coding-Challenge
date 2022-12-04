class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left=list(accumulate(nums))
        right=list(accumulate(nums[::-1]))
        n=len(nums)
        mn=sys.maxsize
        ind=None
        for i in range(n):
            if i==n-1:
                l,r=int(left[i]/(i+1)),0
            else:
                l,r=int(left[i]/(i+1)),int(right[n-i-2]/(n-i-1))
           
            diff=abs(l-r)
            if diff<mn:
                mn=diff
                ind=i
            
        return ind
            
        
        