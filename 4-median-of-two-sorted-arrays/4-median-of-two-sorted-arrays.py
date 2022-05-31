class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        arr=[]
        l=r=i=0
        while l<m and r<n:
            if nums1[l]<=nums2[r]:
                arr.append(nums1[l])
                l+=1
            else:
                arr.append(nums2[r])
                r+=1
        if l<m:
            arr.extend(nums1[l:])
        elif r<n:
            arr.extend(nums2[r:])
            
        if (m+n)&1:
            return arr[(m+n)//2]
        else:
            m1=arr[(m+n)//2]
            m2=arr[(m+n-1)//2]
            return (m1+m2)/2
        