class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        mn=sys.maxsize
        ind=None
        curr=0
        s=sum(nums)
        for i in range(n):
            curr+=nums[i]
            l=curr//(i+1)
            if i!=n-1:
                r=(s-curr)//(n-i-1) 
            else:
                r=0
            diff=abs(l-r)
            if diff<mn:
                mn=diff
                ind=i
            
        return ind
            
        
        