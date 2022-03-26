class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:    
        res=[]
        for el in nums:
            res.append(el**2)
        res.sort()
        return res
        