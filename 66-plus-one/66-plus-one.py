class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=deque()
        n=len(digits)-1
        curr=0
        for el in digits:
            curr+=el*(10**n)
            n-=1
        curr+=1
        while curr:
            res.appendleft(curr%10)
            curr//=10
        return res
            
            
        