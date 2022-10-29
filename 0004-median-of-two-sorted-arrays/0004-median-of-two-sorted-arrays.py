class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        mid=(n1+n2+1)//2
        isEven=(n1+n2)%2==0
        l=0
        r=n1
        while l<=r:
            cut1=l+(r-l)//2
            cut2=mid-cut1
            
            l1=-sys.maxsize if cut1==0 else nums1[cut1-1]
            l2=-sys.maxsize if cut2==0 else nums2[cut2-1]
            r1=sys.maxsize if cut1==n1 else nums1[cut1]
            r2=sys.maxsize if cut2==n2 else nums2[cut2]
            
            if l1<=r2 and l2<=r1:
                if isEven:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            
            elif l1>r2:
                r=cut1-1
            else:
                l=cut1+1
        
                
        
       
            
        
            
            
        