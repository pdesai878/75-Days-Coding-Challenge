# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def findDistance(node,target):
            if not node:
                return -1
            if node.val==target:
                return 0
            left=findDistance(node.left,target)
            right=findDistance(node.right,target)
            dis=max(left,right)
            return dis+1 if dis>=0 else -1
        
        
        def findLCA(node):
            if not node:
                return 
            if node.val==p or node.val==q:
                return node
            left=findLCA(node.left)
            right=findLCA(node.right)
            if left and right:
                return node
            if left:
                return left
            return right
        
            
        lca=findLCA(root)
      
        d1=findDistance(lca,p)
        d2=findDistance(lca,q)
        return d1+d2
        
        