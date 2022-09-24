class Solution:
    def subarraysWithKDistinct(self, s: List[int], k: int) -> int:
        def atmostK(s,k):
            if k==0:
                return 0
            dicti={}
            i=0
            count=0
            n=len(s)
            for j in range(n):
                if s[j] in dicti:
                    dicti[s[j]]+=1
                else:
                    dicti[s[j]]=1
                
                
                while len(dicti)>k and i<n:
                    if s[i] in dicti:
                        dicti[s[i]]-=1
                        if dicti[s[i]]==0:
                            del dicti[s[i]]
                    i+=1
                    
                count+=j-i+1

            return count

        return atmostK(s,k)-atmostK(s,k-1)

            
        