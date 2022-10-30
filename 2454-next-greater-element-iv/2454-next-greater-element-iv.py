class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ngr=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            if not stack:
                ngr[i]=n
            elif stack and nums[stack[-1]]>nums[i]:
                ngr[i]=stack[-1]
            elif stack and nums[stack[-1]]<=nums[i]:
                while stack and nums[stack[-1]]<=nums[i]:
                    stack.pop()
                if not stack:
                    ngr[i]=n
                else:
                    ngr[i]=stack[-1]
            stack.append(i)
        
        ans=[-1]*n
        for i in range(n):
            pos=ngr[i]
            pos+=1
            while pos<n and nums[pos]<=nums[i]:
                pos=ngr[pos]
            if pos<n:
                ans[i]=nums[pos]
            else:
                ans[i]=-1
        return ans
           
        
                
        
        