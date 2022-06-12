class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        def check(pos):
            if pos+k>n:
                return False
            ind=0
            for i in range(pos,pos+k):
                if s[i]==sub[ind] or s[i] in dicti[sub[ind]]:
                    ind+=1
                else:
                    return False
            return True
        
        k=len(sub)
        n=len(s)
        dicti=defaultdict(set)
        for ch,re in mappings:
            dicti[ch].add(re)
        for i in range(n):
            if check(i):
                return True
        return False
            
        