class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node=0,par=None):
            for child in adj[node]:
                if child==par:
                    continue
                dfs(child,node)
                count[node]+=count[child]
                s[node]+=s[child]+count[child]
                
        def dfs2(node = 0, parent = None):
            for child in adj[node]:
                if child != parent:
                    s[child] = s[node] - count[child] + n - count[child]
                    dfs2(child, node)
            
            
        
        
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        s=[0]*n
        count=[1]*n
        dfs()
        dfs2()
        return s
            
        