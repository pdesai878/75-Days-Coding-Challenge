# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def convert(node):
            if not node:
                return
            right=convert(node.right)
            left=convert(node.left)
             
            node.right=self.prev
            node.left=None
            self.prev=node
            
            return node
        
        self.prev=None
        return convert(root)
        
        