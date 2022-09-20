class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #bfs kahn's algo
        adj=defaultdict(list)
        n=numCourses
        indegree=[0]*n
        for v,u in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        q=deque()
        for node in range(n):
            if indegree[node]==0:
                q.append(node)
        courses=0
        while q:
            node=q.popleft()
            courses+=1
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        return courses==numCourses
            
                
            
        