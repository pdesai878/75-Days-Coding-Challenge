# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pre_start,pre_end,in_start,in_end):
            if pre_start>pre_end or in_start>in_end:
                return
            value=preorder[pre_start]
            ind=dicti[value]
            newNode=TreeNode(value)
            newNode.left=build(pre_start+1,pre_start+(ind-in_start),in_start,ind-1)
            newNode.right=build(pre_start+(ind-in_start)+1,pre_end,ind+1,in_end)
            return newNode
        
        dicti={el:i for i,el in enumerate(inorder)}
        n=len(inorder)
        return build(0,n-1,0,n-1)
        
            