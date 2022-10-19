class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]    
        right=[]
        res=[]
        n=len(nums)
        l=r=1
        for i in range(n):
            l*=nums[i]
            r*=nums[n-i-1]
            left.append(l)
            right.append(r)
        right.reverse()
        
        for i in range(n):
            if i==0:
                res.append(right[1])
            elif i==n-1:
                res.append(left[n-2])
            else:
                res.append(left[i-1]*right[i+1])
                
            
            
        
        return res
        