class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small=big=sys.maxsize
        for el in nums:
            if el<=small:
                small=el
            elif el<=big:
                big=el
            else:
                return True
            
           
        return False