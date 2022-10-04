# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(post_start,post_end,in_start,in_end):
            if post_start>post_end or in_start>in_end:
                return
            value=postorder[post_end]
            ind=dicti[value]
            newNode=TreeNode(value)
            newNode.left=build(post_start,post_start+(ind-in_start)-1,in_start,ind-1)
            newNode.right=build(post_start+(ind-in_start),post_end-1,ind+1,in_end)
            return newNode
        
        dicti={el:i for i,el in enumerate(inorder)}
        n=len(inorder)
        return build(0,n-1,0,n-1)
        