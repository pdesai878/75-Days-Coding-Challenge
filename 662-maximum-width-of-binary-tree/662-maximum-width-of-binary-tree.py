# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque()
        mx=1
        q.append([root,0])
        while q:
            n=len(q)
            left=right=None
            for i in range(n):
                node,ind=q.popleft()
                if i==0:
                    left=ind
                if i==n-1:
                    right=ind
                if node.left:
                    q.append((node.left,2*ind+1))
                if node.right:
                    q.append((node.right,2*ind+2))
            mx=max(mx,right-left+1)
        return mx
                    
                             
        