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
                return []
            if not node.left and not node.right:
                return [node.val]
            
            left=postOrder(node.left)
            right=postOrder(node.right)
            
            length=len(left)+len(right)
            if length>self.mx:
                self.path=left+[node.val]+right
                self.mx=length
            
            return max(left,right,key=len)+[node.val]
        
        self.mx=-1
        self.path=[]
        postOrder(root)
        print(self.path)
        return self.mx if self.path else 0
        