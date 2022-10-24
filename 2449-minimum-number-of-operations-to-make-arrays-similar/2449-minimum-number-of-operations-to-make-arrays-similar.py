class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        def getMin(nums,target):
            add=0
            i=j=0
            n=len(nums)
            op=0
            while i<n and j<n:
                if nums[i]<target[j]:
                    add+=(target[j]-nums[i])//2
                    op+=(target[j]-nums[i])//2
                else:
                    add-=(nums[i]-target[j])//2
                i+=1
                j+=1
            return op
        
        
        odd_nums=[el for el in nums if el&1]
        odd_nums.sort()
        even_nums=[el for el in nums if el&1==0]
        even_nums.sort()
        odd_target=[el for el in target if el&1]
        odd_target.sort()
        even_target=[el for el in target if el&1==0]
        even_target.sort()
        
        res=0
        res+=getMin(odd_nums,odd_target)
        res+=getMin(even_nums,even_target)
        return res
        
        
        
        
        
        
            
        
        
                
            
        