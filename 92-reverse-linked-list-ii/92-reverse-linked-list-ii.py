# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy

        for i in range(left-1):
            prev=prev.next
            
        tail=prev.next
       
        for _ in range(right-left):
            temp=prev.next
            prev.next=tail.next
            tail.next=tail.next.next
            prev.next.next=temp
        return dummy.next
            
        
        
      
        
        
            
        
        