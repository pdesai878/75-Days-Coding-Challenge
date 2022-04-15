class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        slow=fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if fast==slow:
                break
           
        #find the entrance point
        slow=nums[0]
        while fast!=slow:
            slow=nums[slow]
            fast=nums[fast]
        return fast

            
        
            
       
                
            
            
        
        