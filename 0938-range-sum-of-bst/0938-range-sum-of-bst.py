# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(node):
            if not node:
                return 0
            left=inorder(node.left)
            s=0
            if low<=node.val<=high:
                s+=node.val
            right=inorder(node.right)
            return left+s+right
        
        return inorder(root)
        