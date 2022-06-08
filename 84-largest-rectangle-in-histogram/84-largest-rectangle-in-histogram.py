class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        nsl,nsr=[],[]
        stack=[]
        n=len(arr)
        #nsl
        for i in range(n):
            el=arr[i]
            if not stack:
                nsl.append(-1)
            elif stack and el>arr[stack[-1]]:
                nsl.append(stack[-1])
            elif stack and el<=arr[stack[-1]]:
                while stack and el<=arr[stack[-1]]:
                    stack.pop()
                if stack:
                    nsl.append(stack[-1])
                else:
                    nsl.append(-1)
            stack.append(i)
        
        #nsr
        stack=[]
        for i in range(n-1,-1,-1):
            el=arr[i]
            if not stack:
                nsr.append(n)
            elif stack and el>arr[stack[-1]]:
                nsr.append(stack[-1])
            elif stack and el<=arr[stack[-1]]:
                while stack and el<=arr[stack[-1]]:
                    stack.pop()
                if stack:
                    nsr.append(stack[-1])
                else:
                    nsr.append(n)
            stack.append(i)
            
        nsr.reverse()
      
        mx=0
        for i in range(n):
            mx=max(mx,(nsr[i]-nsl[i]-1)*arr[i])
        return mx
            
        
        
                
            

            
        
        
        
                
        