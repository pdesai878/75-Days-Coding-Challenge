# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node):
            curr=node
            prev=None
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        
        curr=head
        prev=None
        count=1
        while curr and count!=left:
            prev=curr
            curr=curr.next
            count+=1
        start=curr
        while curr and count!=right:
            curr=curr.next
            count+=1
        rest=curr.next

        curr.next=None
        newHead=reverse(start)
        
        if prev:
            prev.next=newHead
        
        curr=newHead
        while curr.next:
            curr=curr.next
        curr.next=rest
        
        if left==1:
            return newHead
        return head
            
        
        
        
        
        
    
        
        
        
            
        