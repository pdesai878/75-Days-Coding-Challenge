class Trie:
    def __init__(self):
        self.root={}
    def insert(self,word):
        curr=self.root
        for ch in word:
            if ch not in curr:
                curr[ch]={}
            curr=curr[ch]
    def check(self,ch):
        if ch in self.root:
            return True
        return False
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i,j,temp,curr):
            if temp in words:
                res.add(temp)
                
            if len(temp)>mx:
                return False
            
            curr=curr[board[i][j]]
            orig=board[i][j]
            board[i][j]="*"
            for x,y in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
                if 0<=x<row and 0<=y<col and board[x][y] in curr:
                    dfs(x,y,temp+board[x][y],curr)
            board[i][j]=orig
        
        
        
        
        trie=Trie()
        for word in words:
            trie.insert(word)
        row=len(board)
        col=len(board[0])
        mx=len(max(words,key=len))
        res=set()
        words=set(words)
        for i in range(row):
            for j in range(col):
                if trie.check(board[i][j]):
                    dfs(i,j,board[i][j],trie.root)
        return res
        
        