class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.val=-1
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,num):
        node=self.root
       
        for i in range(31,-1,-1):
            bit=(num>>i) & 1
            if bit not in node.children:
                node.children[bit]=TrieNode()
            node=node.children[bit]
        node.val=num
        
            
    def maxXor(self,num):
        node=self.root
        curr=0
        for i in range(31,-1,-1):
            bit=(num>>i) & 1
            opp_bit=1-bit
            if opp_bit in node.children:
                node=node.children[opp_bit]
            else:
                node=node.children[bit]
        
        return num^node.val
                
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root=Trie()
        for el in nums:
            root.insert(el)
        mx=0
        for el in nums:
            mx=max(mx,root.maxXor(el))
        return mx
            
            
        