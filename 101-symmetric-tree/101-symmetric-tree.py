# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left,right):
            q=deque()
            q.append((left,right))
            while q:
                n=len(q)
                for _ in range(n):
                    left,right=q.popleft()
                    if not left or not right:
                        if left==right:
                            continue
                        return False
                    if left.val!=right.val:
                        return False
                    
                    q.append((left.left,right.right))
                    q.append((left.right,right.left))
            return True
            
                    
                    
                
                
        
        return check(root.left,root.right)
          
            
        