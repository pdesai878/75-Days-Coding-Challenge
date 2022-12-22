class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd=math.gcd(*numsDivide)
        for i,a in enumerate(sorted(nums)):
            if gcd % a == 0: return i
            if a > gcd: break
        return -1
        
        
                
        
                
            
            
        