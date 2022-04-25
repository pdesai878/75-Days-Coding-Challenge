# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hA=headA
        hB=headB
        while True:
            if headA==headB:
                return headA
            headA=headA.next if headA else hB
            headB=headB.next if headB else hA
            
        return None
            
        