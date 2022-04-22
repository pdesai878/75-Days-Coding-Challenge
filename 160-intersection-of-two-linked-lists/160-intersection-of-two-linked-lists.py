# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def get_length(head):
            n=1
            while head:
                head=head.next
                n+=1
            return n
        
        n1=get_length(headA)
        n2=get_length(headB)
        
        if n1>n2:
            headA,headB=headB,headA
            n1,n2=n2,n1
            
        diff=n2-n1
        
        p1=headA
        p2=headB
        while diff:
            p2=p2.next
            diff-=1
        
        while p1!=p2:
            p1=p1.next
            p2=p2.next
        return p2
            
            
            