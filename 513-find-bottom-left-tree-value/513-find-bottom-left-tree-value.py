# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def getRightView(node,depth):
            if not node:
                return
            
           
            if self.prevdepth<depth:
                self.res=node.val
                self.prevdepth=depth
                
            getRightView(node.left,depth+1)
            getRightView(node.right,depth+1)
            
        
        self.res=None
        self.prevdepth=-1
        getRightView(root,0)
        return self.res
        