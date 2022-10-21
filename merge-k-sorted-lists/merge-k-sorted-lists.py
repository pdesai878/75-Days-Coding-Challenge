# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            res=dummy=ListNode(-1)
            p1=l1
            p2=l2
            while p1 and p2:
                if p1.val<=p2.val:
                    dummy.next=p1
                    p1=p1.next
                else:
                    dummy.next=p2
                    p2=p2.next
                dummy=dummy.next
            if p1:
                dummy.next=p1
            elif p2:
                dummy.next=p2
            
            return res.next
        
        def mergeK(ind):
            if ind==n:
                return None
            l1=lists[ind]
            l2=mergeK(ind+1)
            merged=merge(l1,l2)
            return merged
        
        n=len(lists)
        return mergeK(0)
            