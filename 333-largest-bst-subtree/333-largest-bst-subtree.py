# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class NodeVal:
    def __init__(self,mn,mx,size):
        self.mx=mx
        self.mn=mn
        self.size=size
        
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        def getLargest(node):
            if not node:
                return NodeVal(sys.maxsize,-sys.maxsize,0)
            
    
            left=getLargest(node.left)
            right=getLargest(node.right)
            
            
            if left.mx<node.val<right.mn:
                return NodeVal(min(node.val,left.mn), max(node.val,right.mx), left.size+right.size+1)
                

            return NodeVal(-sys.maxsize,sys.maxsize,max(left.size,right.size))
        
       
        return getLargest(root).size
        
                
                
            
        