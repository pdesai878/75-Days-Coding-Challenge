TC has to be O(n)
SC : O(n) => set approach: we'll be storing nodes in  a set. While iterating through the list, if the node already exists in the set, then we're sure of a cycle.
```
nodes_seen = set()
while head is not None:
if head in nodes_seen:
return True
nodes_seen.add(head)
head = head.next
return False
```
SC: O(1):  two pointers approach (floyd's cycle detection algo)
=> we'll be maintaining fast and slow pointers.
slow pointer moves one step at a time.
fast pointer moves two step at a time.
​
1)if there's a cycle, fast and slow pointer will eventually collide at certain point.
​
2)if there's no cycle, then fast pointer would be the first to reach the end of linked list.
​
```
nodes_seen = set()
while head is not None:
if head in nodes_seen:
return True
nodes_seen.add(head)
head = head.next
return False
```