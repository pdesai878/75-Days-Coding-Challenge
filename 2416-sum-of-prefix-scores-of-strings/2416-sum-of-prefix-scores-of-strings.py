class TrieNode:
    def __init__(self):
        self.children={}
        self.prefixCount=0
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
            curr.prefixCount+=1
            
    def getPrefixScore(self,word):
        score=0
        curr=self.root
        for ch in word:
            curr=curr.children[ch]
            score+=curr.prefixCount
        return score
            
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie=Trie()
        for word in words:
            trie.insert(word)
        res=[]
        for word in words:
            res.append(trie.getPrefixScore(word))
        return res
        