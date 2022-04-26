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
        
        e=head
        dummy=ListNode(0)
        prev=dummy
        prev.next=head
        i=1
        while e:
            if i%k==0:
                nxt=e.next
                s=prev.next
                reverse(s,e)
                prev.next=e
                s.next=nxt
                prev=s
                e=nxt      
            else:
                e=e.next
            i+=1
        return dummy.next
            
            
    
        
        
            
        
        