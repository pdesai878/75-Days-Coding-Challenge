# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        mid=slow
        if mid.next:
            mid.val=mid.next.val
            mid.next=mid.next.next
        else:
            if head.next:
                head.next=head.next.next
            else:
                return None
        return head
        
        