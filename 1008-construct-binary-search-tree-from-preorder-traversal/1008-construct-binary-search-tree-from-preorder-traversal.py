# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build(bound=sys.maxsize):
            if self.ind>=n or preorder[self.ind]>bound:
                return None
        
            node=TreeNode(preorder[self.ind])
            self.ind+=1
            node.left=build(node.val)
            node.right=build(bound)
            return node
        
        n=len(preorder)
        self.ind=0
        return build()
                
        
            