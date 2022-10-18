# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        if not root:
            return ""
        q=deque()
        q.append(root)
        res=""
        while q:
            node=q.popleft()
            if node:
                res+=str(node.val)+" "
                q.append(node.left)
                q.append(node.right)
            else:
                res+="* "
        return res
    
    def deserialize(self, data):
        if data=='':
            return None
        data=data.split(" ")
        q=deque()
        root=TreeNode(int(data[0]))
        q.append(root)
        itr=1

        while q:
            node=q.popleft()
            if data[itr]!='*':
                node.left=TreeNode(int(data[itr]))
                q.append(node.left)
            itr+=1
            if data[itr]!='*':
                node.right=TreeNode(int(data[itr]))
                q.append(node.right)
            itr+=1
                
        return root
            
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))