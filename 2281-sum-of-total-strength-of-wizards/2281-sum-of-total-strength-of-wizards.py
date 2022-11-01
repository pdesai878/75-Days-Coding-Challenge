class Solution:
    def totalStrength(self, arr: List[int]) -> int:
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
            elif stack and arr[stack[-1]]<=arr[i]:
                nsr.append(stack[-1])
            elif stack and arr[stack[-1]]>arr[i]:
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                if stack:
                    nsr.append(stack[-1])
                else:
                    nsr.append(n)
            stack.append(i)
      
        
        s=0
        p=10**9+7
        nsr.reverse()
        res = 0
        acc = list(accumulate(accumulate(arr), initial = 0))
        for i in range(n):
            l, r = nsl[i], nsr[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += arr[i] * (racc * ln - lacc * rn)
        return res%p
        
        