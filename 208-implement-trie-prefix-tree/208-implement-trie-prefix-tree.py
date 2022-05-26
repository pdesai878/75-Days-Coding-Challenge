class TrieNode:
    def __init__(self):
        self.children=[0]*26
        self.end_word=False
        
class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root
        for ch in word:
            ind=ord(ch)-ord('a')
            if not curr.children[ind]:
                curr.children[ind]=TrieNode()
            curr=curr.children[ind]
        curr.end_word=True
        

    def search(self, word: str) -> bool:
        curr=self.root
        for ch in word:
            ind=ord(ch)-ord('a')
            if not curr.children[ind]:
                return False
            curr=curr.children[ind]
        return True if curr.end_word else False
        
    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for ch in prefix: 
            ind=ord(ch)-ord('a')
            if not curr.children[ind]:
                return False
            curr=curr.children[ind]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)