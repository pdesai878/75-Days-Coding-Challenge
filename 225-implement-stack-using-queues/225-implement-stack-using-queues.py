from collections import deque
class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x: int) -> None:
        #insert x to q2
        self.q2.appendleft(x)
        #insert el by el from q1 to q2 
        while self.q1:
            self.q2.append(self.q1.popleft())
        #swap q1 and q2
        self.q1,self.q2=self.q2,self.q1
        
    def pop(self) -> int:
        return self.q1.popleft()
        
    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return True if not self.q1 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()