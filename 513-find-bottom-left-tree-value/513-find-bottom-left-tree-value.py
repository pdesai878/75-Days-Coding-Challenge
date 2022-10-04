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
            
           
            if depth not in res:
                res[depth]=node.val
                
            getRightView(node.left,depth+1)
            getRightView(node.right,depth+1)
            
        
        res={}
        getRightView(root,0)
        l=list(res.values())
        return l[-1]
        