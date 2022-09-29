class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        s=set()
        n=len(nums)
        for j in range(n):
            if nums[j] in s:
                return True
            s.add(nums[j])
            while i<n and len(s)>k:
                s.remove(nums[i])
                i+=1
        return False
                
            
        