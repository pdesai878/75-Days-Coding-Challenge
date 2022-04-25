# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def length(node):
            l=1
            while node:
                node=node.next
                l+=1
            return l
        
        l1=length(headA)
        l2=length(headB)
        
        if l1<l2:
            headA,headB=headB,headA
            l1,l2=l2,l1
        
        diff=l1-l2
        
        while diff and headA:
            headA=headA.next
            diff-=1
       
        while headA!=headB: 
            headA=headA.next
            headB=headB.next
            
        return headA
        
            
        