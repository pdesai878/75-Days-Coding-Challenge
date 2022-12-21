class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
    
    def findParent(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        p1=self.findParent(u)
        p2=self.findParent(v)
        
        if p1!=p2:
            if self.rank[p1]>self.rank[p2]:
                self.parent[p2]=p1
                self.rank[p1]+=self.rank[p2]
            else:
                self.parent[p1]=p2
                self.rank[p2]+=self.rank[p1]

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        dsu=DSU(n+1)
        adj=defaultdict(list)
        for u,v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
            
        for node in range(1,n+1):
            for neighbor in adj[node]:
                p1=dsu.findParent(node)
                p2=dsu.findParent(neighbor)

                if p1!=p2:
                    dsu.union(adj[node][0],neighbor)
                else:
                    return False
            
        return True
            
        