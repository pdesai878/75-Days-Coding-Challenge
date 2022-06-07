class Node:
    def __init__(self):
        self.key=0
        self.value=0
        self.prev=None
        self.next=None
        self.freq=1
        
class DLL:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        
        self.head.next=self.tail
        self.tail.prev=self.head
        
        self.size=0
        
    def remove_node(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1
        
    def pop_tail(self):
        tail=self.tail.prev
        self.remove_node(tail)
        print("popping",tail.key)
        return tail
    
    def add_node(self,node):
        headNext = self.head.next
        headNext.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        self.size += 1
        
        
    # def move_to_head(self,node):
    #     self.remove_node(node)
    #     self.add_node(node)
        
      
class LFUCache:

    def __init__(self, capacity: int):
        self.cache=defaultdict(DLL)
        self.hashmap={}
        self.capacity=capacity
        self.minFreq=0
        
    def get(self, key: int) -> int:
        node=self.hashmap.get(key,None)
        if not node:
            return -1
        value=node.value
        self.update_cache(node)
        return value
    
    def update_cache(self,node):
        prevFreq=node.freq
        node.freq+=1
        
        self.cache[prevFreq].remove_node(node)
        self.cache[node.freq].add_node(node)
        
        if prevFreq==self.minFreq and self.cache[prevFreq].size==0:
            self.minFreq+=1
            del self.cache[prevFreq]
        print("update_cache",node.key,node.freq)
     
    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return 

        node=self.hashmap.get(key,None)
        if not node:
            newNode=Node()
            newNode.key=key
            newNode.value=value

            self.cache[newNode.freq].add_node(newNode)
            self.hashmap[key]=newNode


            if len(self.hashmap)>self.capacity:
                del_node=self.cache[self.minFreq].pop_tail()
                del self.hashmap[del_node.key]


            self.minFreq=1

        else:
            node.value=value
            self.hashmap[key]=node
            self.update_cache(node)
    
        
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)