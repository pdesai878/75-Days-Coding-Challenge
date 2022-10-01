# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(p1,p2):
            print(p1.val,p2.val)
            curr=p1
            prev=None
            while prev!=p2:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        
        count=1
        prev=None
        curr=head
        while curr and count!=left:
            prev=curr
            curr=curr.next
            count+=1
        start=curr
        while curr and count!=right:
            curr=curr.next
            count+=1
        end=curr
        nxt=curr.next
        end.next=None
        newHead=reverse(start,end)
        
        
        
        if prev:
            prev.next=newHead
        
        curr=newHead
        
        while curr.next:
            curr=curr.next
        curr.next=nxt
        
        if left==1:
            return newHead
        
        return head
        
      
        
        
            
        
        