class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n=len(start)
        m=len(target)
        i=0
        j=0
        while True:
            while i<n and start[i]=="_":
                i+=1
            while j<m and target[j]=="_":
                j+=1
            
            if i==n or j==m:
                return i==n and j==m
            
            if start[i]!=target[j]:
                return False
           
            if target[j]=='L':
                if j>i:
                    return False;
            
            elif target[j]=="R":
                if i>j: 
                    return False
            
            i+=1
            j+=1
        # print(i,j,n,m)
        return True
        
        