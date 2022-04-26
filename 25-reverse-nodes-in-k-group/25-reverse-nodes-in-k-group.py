# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(s,e):
            curr=s
            prev=None
            while prev!=e:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            
        if head is None or head.next is None or k==1:
            return head
        
        
        s=e=head
        for _ in range(k-1):
            e=e.next
            if not e:
                return head
        
        nextHead=self.reverseKGroup(e.next,k)
        reverse(s,e)
        s.next=nextHead
        return e        
        
            
    
        
        
            
        
        