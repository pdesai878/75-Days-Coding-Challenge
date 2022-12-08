# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getSeq(node, res):
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
                return
            getSeq(node.left,res)
            getSeq(node.right,res)
        
        
        leaves1=[]
        leaves2=[]
        getSeq(root1,leaves1)
        getSeq(root2,leaves2)
        
        return leaves1==leaves2
        