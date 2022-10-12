class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node,color):
            visited[node]=color
            
            for neighbor in graph[node]:
                if visited[neighbor]==-1:
                    if not dfs(neighbor,color^1):
                        return False
                elif visited[neighbor]==color:
                    return False
            return True
        visited=[-1 for node in range(len(graph))]
        for node in range(len(graph)):
            if visited[node]==-1:
                temp=dfs(node,0)
                if temp is False:
                    return False
        return True
        