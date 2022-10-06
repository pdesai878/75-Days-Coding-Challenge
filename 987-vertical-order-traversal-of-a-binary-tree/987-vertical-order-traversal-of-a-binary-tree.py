# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def getVerticalTrav(node,dis,depth):
            if node:
                res.append((node.val,dis,depth))
                getVerticalTrav(node.left,dis-1,depth+1)
                getVerticalTrav(node.right,dis+1,depth+1)
        
        res=[]
        getVerticalTrav(root,0,0)
        res.sort(key=lambda x: (x[1],x[2],x[0]))
        distance={}
        for val,dis,level in res:
            if dis not in distance:
                distance[dis]=[val]
            else:
                distance[dis]+=[val]
        return distance.values()
            
        
        
        
            