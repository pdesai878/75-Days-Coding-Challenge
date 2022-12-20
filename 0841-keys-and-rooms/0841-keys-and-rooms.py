class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        visited=[False for _ in range(n)]
        
        q=deque()
        q.append(0)
        visited[0]=True
        while q:
            curr=q.popleft()
            n-=1
            for neigh in rooms[curr]:
                if not visited[neigh]:
                    q.append(neigh)
                    visited[neigh]=True
        return n==0
                
        
        
        
                
            
            
            
        