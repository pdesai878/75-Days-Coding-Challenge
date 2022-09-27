# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.p=0
        #brute force
        def get_inorder(node):
            if not node:
                return
            get_inorder(node.left)
            inorder.append(node.val)
            get_inorder(node.right)
            
        def recover(node):
            if not node:
                return
            recover(node.left)
            if node.val!=inorder[self.p]:
                node.val=inorder[self.p]
            self.p+=1
            recover(node.right)
            
        inorder=[]
        get_inorder(root)
        inorder.sort()
        
        recover(root)
        
        return root
        