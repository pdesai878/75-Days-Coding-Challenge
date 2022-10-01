# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if root.val<node.val<self.res:
                self.res=node.val
            inorder(node.right)
            
       
        self.res=sys.maxsize
        inorder(root)
        return self.res if self.res!=sys.maxsize else -1
        