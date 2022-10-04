class Node:
    def __init__(self):
        self.key=None
        self.val=None
        self.next=None
        self.prev=None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.size=0
        
        self.head=Node()
        self.tail=Node()
        
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def remove_node(self,node):
        prev=node.prev
        nxt=node.next
        
        prev.next=nxt
        nxt.prev=prev
        
    def add_node(self,node):
        node.prev=self.head
        node.next=self.head.next
        
        self.head.next.prev=node
        self.head.next=node
        
    
    def move_to_head(self,node):
        self.remove_node(node)
        self.add_node(node)
        
    def pop_tail(self):
        node=self.tail.prev
        self.remove_node(node)
        return node
        
    def get(self, key: int) -> int:
        node=self.cache.get(key,None)
        if node:
            self.move_to_head(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        node=self.cache.get(key,None)
        if not node:
            newNode=Node()
            newNode.key=key
            newNode.val=value
            
            self.cache[key]=newNode
            self.add_node(newNode)
            self.size+=1
            
            if self.size>self.capacity:
                tail=self.pop_tail()
                del self.cache[tail.key]
                self.size-=1
        else:
            node.val=value
            self.move_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)