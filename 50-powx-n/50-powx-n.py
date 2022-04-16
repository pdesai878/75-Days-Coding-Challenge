class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        neg=False
        if n<0:
            neg=True
            n=abs(n)
        while n:
            if n&1:
                n-=1
                res*=x
            else:
                x*=x
                n//=2
        if neg:
            return 1/res
        return res
                
            