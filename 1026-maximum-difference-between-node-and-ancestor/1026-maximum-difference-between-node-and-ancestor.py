# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def getMax(node,mx,mn):
            if not node:
                return abs(mx-mn)
                 
            mx=max(mx,node.val)
            mn=min(mn,node.val)
            
            left=getMax(node.left,mx,mn)
            right=getMax(node.right,mx,mn)
            
            return max(left,right)
            
        
        return getMax(root,root.val,root.val)
       
        