class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def rev(no):
            n=str(no)
            return int(n[::-1])
        
        target=num
        for no in range(num+1):
            if no+rev(no)==target:
                return True
        return False
        