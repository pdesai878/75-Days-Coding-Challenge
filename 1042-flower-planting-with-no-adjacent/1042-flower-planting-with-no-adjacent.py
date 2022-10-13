class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        def isPossible(node,c):
            for neighbor in adj[node]:
                if color[neighbor]==c:
                    return False
            return True
        
        def dfs(node,c):
            if node==n+1:
                return True
            orig=color[node]
            for colr in range(1,5):
                if isPossible(node,colr):
                    color[node]=colr
                    temp=dfs(node+1,colr)
                    if temp:
                        return True
                    color[node]=orig
            return False
                
        adj=defaultdict(list)
        for u,v in paths:
            adj[u].append(v)
            adj[v].append(u)
        color=[-1 for node in range(n+1)]
        for node in range(1,n+1):
            if color[node]==-1:
                temp=dfs(node,1)
                if temp:
                    return color[1:]
        
        