class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
       
        
class Trie:
    def __init__(self,n):
        self.root=TrieNode()
        self.n=n
        
    def insert(self,num):
        node=self.root
       
        for i in range(self.n,-1,-1):
            bit=(num>>i) & 1
            if bit not in node.children:
                node.children[bit]=TrieNode()
            node=node.children[bit]
        
        
            
    def maxXor(self,num):
        if not self.root: 
            return -1
        p, ans = self.root, 0
        for i in range(self.n, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p.children:
                p = p.children[1 - cur]
                ans |= (1 << i)
            else:
                p = p.children[cur]
        return ans
        
        
                
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def bin_len(no):
            count=0
            while no:
                count+=1
                no>>=1
            return count
        
        n = bin_len(max(nums))
        root=Trie(n)
        for el in nums:
            root.insert(el)
        mx=0
        for el in nums:
            mx=max(mx,root.maxXor(el))
        return mx
            
            
        