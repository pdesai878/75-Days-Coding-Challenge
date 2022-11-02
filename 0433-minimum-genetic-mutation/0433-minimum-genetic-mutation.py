class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def isPossible(str1,str2):
            count=0
            for i in range(8):
                if str1[i]!=str2[i]:
                    count+=1
            return count<2
            
        
        n=len(start)
        visited=[False for _ in range(len(bank))]
        q=deque()
        q.append((start,0))
        while q:
            string,count=q.popleft()
            if string==end:
                return count
            for ind,s in enumerate(bank):
                if not visited[ind]:
                    if isPossible(string,s):
                        q.append((s,count+1))
                        visited[ind]=True
        return -1
            
       
            
            
        