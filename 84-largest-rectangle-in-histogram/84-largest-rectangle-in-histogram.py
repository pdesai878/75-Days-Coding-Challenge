class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n=len(arr)
        nsl=[]
        nsr=[]
        stack=[]
        for i in range(n):
            if not stack:
                nsl.append(-1)
            elif stack and arr[stack[-1]]<arr[i]:
                nsl.append(stack[-1])
            elif stack and arr[stack[-1]]>=arr[i]:
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if stack:
                    nsl.append(stack[-1])
                else:
                    nsl.append(-1)
            stack.append(i)
            
        stack.clear()
        
        for i in range(n-1,-1,-1):
            if not stack:
                nsr.append(n)
            elif stack and arr[stack[-1]]<arr[i]:
                nsr.append(stack[-1])
            elif stack and arr[stack[-1]]>=arr[i]:
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if stack:
                    nsr.append(stack[-1])
                else:
                    nsr.append(n)
                    
            stack.append(i)
            
        nsr.reverse()
 
        mx=-sys.maxsize
        for i in range(n):
            width=nsr[i]-nsl[i]-1
            area=arr[i]*width
            mx=max(mx,area)
        return mx
        
                
       
            
                    
                    
            
        