class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        ans=[]
        dicti={nums2[i]:i for i in range(n)}
        stack=[]
        for ind in range(n-1,-1,-1):
            el=nums2[ind]
            if not stack:
                dicti[el]=-1   
            elif stack and stack[-1]>el:
                dicti[el]=stack[-1]
            elif stack and stack[-1]<=el:
                while stack and stack[-1]<=el:
                    stack.pop()
                if stack:
                    dicti[el]=stack[-1]
                else:
                    dicti[el]=-1
            stack.append(el)
           
        for j in nums1:
            ans.append(dicti[j])
        return ans
        
                
            
                
                
                
                
            
        
        