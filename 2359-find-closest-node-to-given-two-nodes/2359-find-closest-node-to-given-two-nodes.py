class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(src,distance):
            visited=[False]*n
            distance[src]=0
            q=set()
            q.add((0,src))
            visited[src]=True
            
            while q:
                d,node=q.pop()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor]=True
                        distance[neighbor]=d+1
                        q.add((distance[neighbor],neighbor))
                        
        
        n=len(edges)
        adj=defaultdict(list)
        for u,v in enumerate(edges):
            if v!=-1:
                adj[u].append(v)
        
        distance1=defaultdict(lambda:sys.maxsize)
        distance2=defaultdict(lambda:sys.maxsize)
        
        bfs(node1,distance1)
        bfs(node2,distance2)
        
        mn=sys.maxsize
        ans=-1
        
        for node in range(n):
            d=max(distance1[node],distance2[node])
            if d<mn:
                mn=d
                ans=node
            elif d==mn:
                ans=min(ans,node)
        return ans
        
        
        
        