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
        if not head:
            return
        #merge lists
        l1=head
        while l1:
            copy=Node(l1.val)
            nxt=l1.next
            l1.next=copy
            copy.next=nxt
            l1=nxt
        #make random connections
        l1=head
        while l1:
            if l1.random:
                l1.next.random=l1.random.next
            l1=l1.next.next
            
        #detach lists
        temp=head
        dummy=Node(-1)
        tail=dummy
        while temp:
            tail.next=temp.next
            tail=tail.next
            
            temp.next=tail.next
            temp=temp.next
        return dummy.next
        
        
      
        
       
        