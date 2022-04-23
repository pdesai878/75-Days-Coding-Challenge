class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        neg=False
        if n<0:
            n=abs(n)
            neg=True
        while n:
            if n&1:
                res*=x
                n-=1
            else:
                x*=x
                n//=2
        if neg:
            return 1/res
        return res
                
            