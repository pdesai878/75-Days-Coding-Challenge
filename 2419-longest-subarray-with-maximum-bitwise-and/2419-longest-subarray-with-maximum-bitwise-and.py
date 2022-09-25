class Solution:
    def longestSubarray(self, arr: List[int]) -> int:
        maxNo=max(arr)
        mx=1
        curr=0
        for el in arr:
            if el==maxNo:
                curr+=1
            else:
                curr=0
            mx=max(mx,curr)
        return mx
            
         
       
         
     
        