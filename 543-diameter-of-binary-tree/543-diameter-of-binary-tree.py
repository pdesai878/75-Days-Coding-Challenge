# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def postOrder(node):
            if not node:
                return 0
            left=postOrder(node.left)
            right=postOrder(node.right)
            
            self.mx=max(self.mx,left+right)
            
            return max(left,right)+1
        
        self.mx=-1
        postOrder(root)
        return self.mx
        