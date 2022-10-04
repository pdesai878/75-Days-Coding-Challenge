# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def getMinDiff(node):
            if not node:
                return
            getMinDiff(node.left)
            if self.prev:
                self.mn=min(self.mn,abs(node.val-self.prev.val))
            self.prev=node
            getMinDiff(node.right)
                
                
        self.prev=None   
        self.mn=sys.maxsize
        getMinDiff(root)
        return self.mn
        