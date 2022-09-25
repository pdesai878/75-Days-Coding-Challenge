class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        def find(node):
            if parent[node]==node:
                return node
            parent[node]=find(parent[node])
            return parent[node]
 
        
        n=len(vals)
        maxV=[vals[i] for i in range(n)]
        freq=[1 for i in range(n)]
        parent=[i for i in range(n)]
        
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        
        ans=n
        for u,v in edges:
            p1=find(u)
            p2=find(v)
            
            if maxV[p1]==maxV[p2]:
                ans+=freq[p1]*freq[p2]
                parent[p2]=p1
                freq[p1]+=freq[p2]
            else:
                if maxV[p1]>maxV[p2]:
                    parent[p2]=p1
                else:
                    parent[p1]=p2
        return ans
                    
                
                
                
        
                
                
            
        