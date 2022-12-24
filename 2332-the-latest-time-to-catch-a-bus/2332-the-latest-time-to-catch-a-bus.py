class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        j=0
        n=len(buses)
        m=len(passengers)
        for i in range(n):
            count=0
            while j<m and passengers[j]<=buses[i] and count<capacity:
                count+=1
                j+=1
            
            if i==n-1:
                if count<capacity:
                    no=buses[i]
                else:
                    no=passengers[j-1]
                p=j-1
                while no:
                    if passengers[p]!=no:
                        return no
                    no-=1
                    p-=1
                
                
                
            
        
       
            
                    
                    
            
        