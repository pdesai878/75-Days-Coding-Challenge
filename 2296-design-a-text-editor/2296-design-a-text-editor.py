class TextEditor:

    def __init__(self):
        self.left=[]
        self.right=[]
        

    def addText(self, text: str) -> None:
        for ch in text:
            self.left.append(ch)
        

    def deleteText(self, k: int) -> int:
        count=0
        while self.left and k:
            self.left.pop()
            k-=1
            count+=1
        return count
       
    
    def cursorLeft(self, k: int) -> str:
        while self.left and k:
            self.right.append(self.left.pop())
            k-=1
        return self.shiftCursor()
        
    
    def cursorRight(self, k: int) -> str:
        while self.right and k:
            self.left.append(self.right.pop())
            k-=1
        return self.shiftCursor()
    
    def shiftCursor(self):
        string=""
        count=10
        while self.left and count:
            string+=self.left.pop()
            count-=1
        string=string[::-1]
        for ch in string:
            self.left.append(ch)
        return string
            
        
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)