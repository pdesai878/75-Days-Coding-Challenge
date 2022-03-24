class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti={}
        for ind,el in enumerate(nums):
            if target-el in dicti:
                return dicti[target-el],ind
            dicti[el]=ind
        
       
        