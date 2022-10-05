# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count=0
        curr=root
        while curr:
            if curr.left:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                    
                if prev.right==curr:
                    count+=1
                    if count==k:
                        return curr.val
                    prev.right=None
                    curr=curr.right
                elif prev.right is None:
                   
                    prev.right=curr
                    curr=curr.left
            else:
                count+=1
                if count==k:
                    return curr.val
                

                curr=curr.right
        
        
        