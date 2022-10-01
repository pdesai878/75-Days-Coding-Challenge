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
            
        def reverseK(node):
            if not node:
                return
            start=end=node
            for _ in range(k-1):
                end=end.next
                if not end:
                    return start
            nxt=end.next
            reverse(start,end)
            start.next=reverseK(nxt)
            return end
                
        return reverseK(head)
            
            
    
        
        
            
        
        