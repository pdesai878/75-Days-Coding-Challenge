class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        skills.sort()
        res=0
        n=len(skills)
        s=None
        res=0
      
        for i in range(n//2):
            curr=skills[i]+skills[n-i-1]
          
            if not s:
                s=curr
                
            elif s!=curr:
                return -1
                
            res+=skills[i]*skills[n-i-1]
        return res
        
        