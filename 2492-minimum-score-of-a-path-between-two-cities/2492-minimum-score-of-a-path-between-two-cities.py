class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def dfs(node):
            visited[node]=True
            mn=10**4+1
            for neighbor,wt in adj[node].items():
                mn=min(mn,wt)
                if not visited[neighbor]:
                    mn=min(mn,dfs(neighbor))
            return mn
        
        adj=defaultdict(dict)
        for u,v,wt in roads:
            adj[u][v]=wt
            adj[v][u]=wt
        
        visited=[False for node in range(n+1)]
        return dfs(1)
        