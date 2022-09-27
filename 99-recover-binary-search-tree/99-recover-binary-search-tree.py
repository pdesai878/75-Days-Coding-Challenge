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
            if self.prev and node.val<self.prev.val:
                if self.first is None:
                    self.first=self.prev
                    self.mid=node
                else:
                    self.last=node
            self.prev=node
            inorder(node.right)
                
        
        self.prev=TreeNode(-sys.maxsize)
        self.first=self.mid=self.last=None
        inorder(root)
        if self.first and self.last:
            self.first.val,self.last.val=self.last.val,self.first.val
        elif self.first and self.mid:
            self.first.val,self.mid.val=self.mid.val,self.first.val
        return root
            
        