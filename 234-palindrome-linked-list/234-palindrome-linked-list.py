# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(curr):
            prev=None
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
            
        def find_middle_el(node):
            fast=slow=node
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        
        if not head or not head.next:
            return head
        
        mid=find_middle_el(head)
        
        next_=reverse(mid.next)
      
        p2=next_
        p1=head
        
        result=True
        while p2:
            if p2.val!=p1.val:
                result=False
            p1=p1.next
            p2=p2.next
            
        return result
        