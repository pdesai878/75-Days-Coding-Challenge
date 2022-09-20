class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dfs
        def dfs(node):
            visited[node]=True
            dfsVisited[node]=True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif dfsVisited[neighbor]:
                    return True
            dfsVisited[node]=False
            return False
        
        adj=defaultdict(list)
        n=numCourses
        for v,u in prerequisites:
            adj[u].append(v)
        visited=[False for node in range(n)]
        dfsVisited=[False for node in range(n)]
        topo=[]
        for node in range(n):
            if not visited[node]:
                if dfs(node):
                    return False
        return True
        
        
        
            
                
            
        