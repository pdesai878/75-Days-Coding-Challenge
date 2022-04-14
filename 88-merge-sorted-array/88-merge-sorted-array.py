class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1=0
        p2=0
        
        
        while p1<m and p2<n:
            if nums1[p1]<=nums2[p2]:
                pass
            else:
                nums1[p1],nums2[p2]=nums2[p2],nums1[p1]
                orig=p2
                while p2<n-1 and nums2[p2]>nums2[p2+1]:
                    nums2[p2],nums2[p2+1]=nums2[p2+1],nums2[p2]
                    p2+=1
                p2=orig
            p1+=1
            print(nums1)
            print(nums2)
            print("\n")
            
        while p2<n:
            nums1[p1]=nums2[p2]
            p2+=1
            p1+=1
    
        
                
       
    