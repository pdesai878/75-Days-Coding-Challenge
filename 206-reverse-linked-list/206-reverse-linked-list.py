# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr,prev):
            if not curr:
                return prev
            nxt=curr.next
            curr.next=prev
            prev=curr
            return reverse(nxt,prev)
        
        head=reverse(head,None)
        return head
            
        