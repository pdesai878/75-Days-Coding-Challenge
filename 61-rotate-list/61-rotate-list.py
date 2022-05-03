# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head
        fast=slow=head
        n=1
        while fast.next:
            fast=fast.next
            n+=1
        k=k%n
        fast.next=head
        
        while n-k-1:
            slow=slow.next
            k+=1
            
        newHead=slow.next
        slow.next=None
        return newHead
            
        
            
        
        
        
       
            
        
        