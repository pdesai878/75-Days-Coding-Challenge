class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node,d):
            if node!=-1:
                if not visited[node]:
                    curr_call.add(node)
                    visited[node]=True
                    distance[node]=d
                    neighbor=edges[node]
                    dfs(neighbor,d+1)
                elif node in curr_call:
                    self.ans=max(self.ans,d-distance[node])

            
            
        n=len(edges)
        visited=[False]*n
        distance=[sys.maxsize]*n
        self.ans=-1
        for node in range(n):
            if not visited[node]:
                curr_call=set()
                dfs(node,0)
        return self.ans
                
                
            
        
        