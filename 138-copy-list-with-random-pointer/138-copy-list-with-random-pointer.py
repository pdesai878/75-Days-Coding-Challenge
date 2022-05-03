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
        dicti={}
        temp=head
        while temp:
            dicti[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if temp.next:
                dicti[temp].next=dicti[temp.next]
            if temp.random:
                dicti[temp].random=dicti[temp.random]
            temp=temp.next
        return dicti[head]
        
        
      
        
       
        