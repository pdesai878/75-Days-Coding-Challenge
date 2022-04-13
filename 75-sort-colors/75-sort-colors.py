class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red_cnt=white_cnt=blue_cnt=0
        for el in nums:
            if el==0: red_cnt+=1
            elif el==1: blue_cnt+=1
            else: white_cnt+=1
        
        i=0
        while red_cnt:
            nums[i]=0
            i+=1
            red_cnt-=1
        while blue_cnt:
            nums[i]=1
            i+=1
            blue_cnt-=1
        while white_cnt:
            nums[i]=2
            i+=1
            white_cnt-=1
        return nums
        
        
            