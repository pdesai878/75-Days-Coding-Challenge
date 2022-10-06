class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        
        n=len(nums1)
        m=len(nums2)
        
        
        isEven=True
        if (n+m)&1:
            isEven=False
            
        l=0
        r=n
        mid=(n+m+1)//2
        inf=sys.maxsize
        while l<=r:
            cut1=(l+r)//2
            cut2=mid-cut1
            
            l1=-inf if cut1==0 else nums1[cut1-1]
            l2=-inf if cut2==0 else nums2[cut2-1]
            r1=inf if cut1==n else nums1[cut1]
            r2=inf if cut2==m else nums2[cut2]
            
            if l1<=r2 and l2<=r1:
                if isEven:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            
            if l1>r2:
                r=cut1-1
            else:
                l=cut1+1
        return 0
        
                
            
        