# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def getMax(node):
            if not node:
                return 0
            left=getMax(node.left)
            right=getMax(node.right)
            curr=left+right+node.val
            self.mx=max(self.mx,(total-curr)*curr)
            return curr
        
        
        def getSum(node):
            if not node:
                return 0
            left=getSum(node.left)
            right=getSum(node.right)
            return left+right+node.val
        
        total=getSum(root)
        self.mx=-1
        getMax(root)
        return self.mx % (10 ** 9 + 7)
        