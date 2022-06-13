# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    @lru_cache(None)
    def cachedknows(self,a,b):
        return knows(a,b)
    
    def findCelebrity(self, n: int) -> int:
        candidate=0
        self.n=n
        for i in range(1,n):
            if self.cachedknows(candidate,i):
                candidate=i
        return candidate if self.is_celebrity(candidate) else -1
    
    def is_celebrity(self,i):
        for j in range(self.n):
            if i==j:
                continue
            if self.cachedknows(i,j) or not self.cachedknows(j,i):
                return False
        return True
                
        
                
        