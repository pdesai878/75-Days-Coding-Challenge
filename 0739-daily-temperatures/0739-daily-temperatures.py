class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ngl=[]
        stack=[]
        n=len(temperatures)
        for i in range(n-1,-1,-1):
            if not stack:
                ngl.append(0)
            elif stack and temperatures[stack[-1]]>temperatures[i]:
                ngl.append(stack[-1])
            elif stack and temperatures[stack[-1]]<=temperatures[i]:
                while stack and temperatures[stack[-1]]<=temperatures[i]:
                    stack.pop()
                if stack:
                    ngl.append(stack[-1])
                else:
                    ngl.append(0)
            stack.append(i)
            
        ans=[]
        
        ngl.reverse()
        for i in range(n):
            if ngl[i]==0:
                ans.append(0)
            else:
                ans.append(abs(i-ngl[i]))
        return ans
                
        