# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
            
        def recover(node):
            if not node:
                return
            recover(node.left)
            if node.val!=arr[self.p]:
                node.val=arr[self.p]
            self.p+=1
            recover(node.right)
            
        
        arr=[]
        inorder(root)
        arr.sort()
       
        self.p=0
        recover(root)
        return root
        