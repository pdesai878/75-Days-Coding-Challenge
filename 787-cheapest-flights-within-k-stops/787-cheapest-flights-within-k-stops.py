class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,wt in flights:
            adj[u].append((v,wt))
        q=deque()
        distance=[sys.maxsize for node in range(n)]
        q.append((src,0))
        distance[src]=0
        level=-1
        while q and level<k:
            count=len(q)
            
            for _ in range(count):
                node,dis=q.popleft()
                
                for neighbor,wt in adj[node]:
                    
                    if dis+wt<distance[neighbor]:
                        distance[neighbor]=dis+wt
                        q.append((neighbor,distance[neighbor]))

            level+=1
        # print(distance)
        return -1 if distance[dst]==sys.maxsize else distance[dst]
            
            
            
            
        
                    
        