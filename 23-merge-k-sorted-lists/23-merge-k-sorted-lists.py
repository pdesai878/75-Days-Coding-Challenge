# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            res=dummy=ListNode(-1)
            while l1 and l2:
                if l1.val<=l2.val:
                    dummy.next=l1
                    l1=l1.next
                else:
                    dummy.next=l2
                    l2=l2.next
                dummy=dummy.next
            if l1:
                dummy.next=l1
            elif l2:
                dummy.next=l2
            return res.next
                    
            
        def mergelists(ind):
            if ind==n:
                return None
            
            if ind==n-1:
                return lists[ind]
            
            l1=lists[ind]
            l2=mergelists(ind+1)
            
            l=merge(l1,l2)
            
            return l
        
        n=len(lists)
        return mergelists(0)
            
            
            
            
        