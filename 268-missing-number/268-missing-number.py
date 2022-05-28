class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        #bit manipulation
        n=len(arr)
        missing_no=n
        for ind,el in enumerate(arr):
            missing_no^=ind^el
        return missing_no