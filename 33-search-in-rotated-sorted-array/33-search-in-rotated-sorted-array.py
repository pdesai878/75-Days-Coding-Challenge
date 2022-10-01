class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPeak(l,r):
            pivot=-1
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]>=nums[0]:
                    pivot=mid
                    l=mid+1
                else:
                    r=mid-1
            return pivot
                    
        def find(l,r):
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return -1
            
            
        n=len(nums)
        peak=findPeak(0,n-1)
        bs1=find(0,peak)
        if bs1!=-1:
            return bs1
        bs2=find(peak+1,n-1)
        if bs2!=-1:
            return bs2
        return -1
        