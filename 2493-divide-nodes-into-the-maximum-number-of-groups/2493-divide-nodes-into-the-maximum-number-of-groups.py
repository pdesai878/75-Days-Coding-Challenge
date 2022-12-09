class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def checkBipartite(graph):
            def bfs(src,c):
                q=deque()
                q.append((src,c))
                color[src]=c
                while q:
                    node,c=q.popleft()
                    components[node]=src
                    for neighbor in adj[node]:
                        if color[neighbor]==-1:
                            q.append((neighbor,c^1))
                            color[neighbor]=c^1
                        elif color[neighbor]==c:
                            return False
                return True
                            
   
            color=[-1]*(n+1)
            for node in range(1,n+1):
                if color[node]==-1:
                    temp=bfs(node,0)
                    if not temp:
                        return False
            return True
        
        
        def bfs(node):
            visited=[False]*(n+1)
            q=deque()
            q.append(node)
            visited[node]=True
            level=0
            while q:
                count=len(q)
                for _ in range(count):
                    node=q.popleft()
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            q.append(neighbor)
                            visited[neighbor]=True
                level+=1
            return level
            

        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        components=[-1]*(n+1)
        if not checkBipartite(adj):
            return -1
        
        comp=[0]*(n+1)
        for node in range(1,n+1):
            levels=bfs(node)
            comp[components[node]]=max(comp[components[node]],levels)
            
        return sum(comp)
                
            
        
        