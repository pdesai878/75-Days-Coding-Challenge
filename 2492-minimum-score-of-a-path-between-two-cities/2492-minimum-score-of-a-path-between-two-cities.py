class DSU:
    def __init__(self,n):
        self.n=n
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
            if self.rank[p1]>=self.rank[p2]:
                self.parent[p2]=p1
                self.rank[p1]+=self.rank[p2]
            else:
                self.parent[p1]=p2
                self.rank[p2]+=self.rank[p1]
                

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu=DSU(n)
       
        for u,v,wt in roads:
            dsu.union(u,v)   
        
        self.mn=10**4+1
        x=dsu.findParent(1)
        for u,v,wt in roads:
            p1=dsu.findParent(u)
            p2=dsu.findParent(v)
            
            if p1==x or p2==x:
                self.mn=min(self.mn,wt)
        return self.mn
                
            
        
        
        
        
        
        
        
        
        