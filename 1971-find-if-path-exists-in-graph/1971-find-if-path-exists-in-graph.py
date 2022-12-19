class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            visited[node]=True
            if node==destination:
                return True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False
        
        
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*n
        return dfs(source)        