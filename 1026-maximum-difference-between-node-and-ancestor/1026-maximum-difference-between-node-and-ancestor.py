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
                self.ans=max(self.ans,abs(mx-mn))
                return
                
            mx=max(mx,node.val)
            mn=min(mn,node.val)
            
            getMax(node.left,mx,mn)
            getMax(node.right,mx,mn)
            
        self.ans=-sys.maxsize
        getMax(root,root.val,root.val)
        return self.ans
        