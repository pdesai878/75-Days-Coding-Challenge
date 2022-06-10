class MinStack:

    def __init__(self):
        self.stack=[]
        self.mn=10**31
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.mn=val
            self.stack.append(val)
            
        elif self.stack:
            if val<self.mn:
                self.stack.append(val*2-self.mn)
                self.mn=val
            else:
                self.stack.append(val)   

    def pop(self) -> None:
        if self.stack:
            el=self.stack.pop()
            if el<self.mn:
                self.mn=2*self.mn-el
        return
        

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1] if self.stack[-1]>self.mn else self.mn
        

    def getMin(self) -> int:
        return self.mn
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()