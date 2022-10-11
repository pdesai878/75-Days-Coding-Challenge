# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #top down approach
        def getMax(node,mn,mx):
            if not node:
                return mx-mn
            mx=max(mx,node.val)
            mn=min(mn,node.val)
            
            return max(getMax(node.left,mn,mx), getMax(node.right,mn,mx))
        
        return getMax(root,root.val,root.val)
            
            
        
        
        
        