class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        p=10**9+7
        binary=str(bin(n))[2:][::-1]
        powers=[2**(i) for i,bit in enumerate(binary) if bit=="1"]
        res=[]
        for r1,r2 in queries:
            temp=1
            for i in range(r1,r2+1):
                temp*=powers[i]
            res.append(temp%p)
        return res
                
        
                
            
        