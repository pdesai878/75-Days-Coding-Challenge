class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        
        s=0
        e=(row*col)-1
        while s<=e:
            mid=s+(e-s)//2
            
            r=mid//col
            c=mid%col
            
            if matrix[r][c]==target:
                return True
            
            elif matrix[r][c]<target:
                s=mid+1
            else:
                e=mid-1
        return False
                    
        