class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        res=[]
        n=len(arr)
        if k>n:
            return res
        i=0
        q=deque()
        for j in range(n):
            el=arr[j]
            while q and q[-1]<el and i<n:
                q.pop()
            q.append(el)
            if j-i+1==k:
                res.append(q[0])
                if arr[i]==q[0]:
                    q.popleft()
                i+=1
        return res
                
                
            