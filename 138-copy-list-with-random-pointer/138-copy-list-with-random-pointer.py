"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #insert new nodes in betweeen
        l1=head
        while l1:
            copy=Node(l1.val)
            nxt=l1.next
            l1.next=copy
            copy.next=nxt
            l1=nxt
        #create links
        l1=head
        while l1:
            if l1.random:
                l1.next.random=l1.random.next
            l1=l1.next.next
        #detach
        tail=dummy=Node(-1)
        while head:
            tail.next=head.next
            tail=tail.next
            
            head.next=tail.next
            head=head.next
        return dummy.next
            
            
            
        