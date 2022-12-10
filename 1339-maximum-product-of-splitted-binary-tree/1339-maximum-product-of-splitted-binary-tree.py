# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def getSum(node):
            if not node:
                return 0
            left=getSum(node.left)
            right=getSum(node.right)
            s=left+right+node.val
            sums.append(s)
            return s
        
        sums=[]
        total=getSum(root)
        mx=-1
        for s in sums:
            mx=max(mx,s*(total-s))
        return mx%(10**9+7)
        
        
        
        