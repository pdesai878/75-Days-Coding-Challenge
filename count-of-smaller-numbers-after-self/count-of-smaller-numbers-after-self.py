class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def insert(el):
            bisect.insort(temp,el)
                      
        n=len(nums)
        res=[0]*n
        temp=[]
        for i in range(n-1,-1,-1):
            if i==n-1:
                res[i]=0
            else:
                count=bisect.bisect_left(temp,nums[i])
                res[i]=count
            insert(nums[i])
        return res
            
            
        