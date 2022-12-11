# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getMax(node):
            if not node:
                return 0
            
            left=getMax(node.left)
            right=getMax(node.right)
            
            curr=max(left,right)+node.val
     
            self.mx=max(self.mx,curr,left+right+node.val,node.val)
            return max(curr,node.val)
        
        self.mx=-sys.maxsize
        getMax(root)
        return self.mx
        