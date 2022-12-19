class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        groups=[]
        size=0
        i=0
        count=0
        n=len(grades)
        while i<n:
            size+=1
            group=[]
            if i+size<=n:
                for j in range(i,i+size):
                    group.append(grades[j])
                groups.append(group)
                i=i+size
                count+=1
            else:
                for j in range(i,n):
                    groups[-1].append(grades[j])
                i=n
           
            
       
        return count
                    
        