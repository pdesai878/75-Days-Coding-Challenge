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
            
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy
        curr=head
        count=1
        while curr:
            if count%k==0:
                nxt=curr.next
                start=prev.next
                end=curr
                
                
                reverse(start,end)
                
                prev.next=end
                start.next=nxt
                prev=start
                
                curr=nxt
            else:
                curr=curr.next
            count+=1
        return dummy.next
            
            
                
        
            
            
    
        
        
            
        
        