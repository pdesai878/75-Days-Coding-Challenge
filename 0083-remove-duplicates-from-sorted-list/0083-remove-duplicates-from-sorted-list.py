# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        while head:
            curr=head
            while curr.next and curr.val==curr.next.val:
                curr=curr.next
            if curr!=head:
                head.next=curr.next
            head=head.next
        return dummy
                
            
        