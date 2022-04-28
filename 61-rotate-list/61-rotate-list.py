# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head
        
        p2=head
        n=1
        while p2.next:
            n+=1
            p2=p2.next
        p2.next=head
        
        k=k%n
        
        p1=head
        
        while n-k-1:
            p1=p1.next
            k+=1
        
        res=p1.next
        p1.next=None
        
        return res
        
            
        
        