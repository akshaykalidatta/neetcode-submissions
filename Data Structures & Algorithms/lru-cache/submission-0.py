class Node:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dct = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, curr: Node):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        curr.next = curr.prev = None

    def insert(self, curr: Node):
        curr.next = self.tail
        curr.prev = self.tail.prev
        self.tail.prev.next = curr 
        self.tail.prev = curr



    def get(self, key: int) -> int:
        if key in self.dct:
            curr = self.dct[key]
        else: return -1

        self.remove(curr)
        self.insert(curr)

        return curr.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            curr = self.dct[key]
            self.remove(curr)
            self.insert(curr)
            curr.val = value
        else:
            curr = Node(value, key)
            self.insert(curr)
            self.dct[key] = curr
            
        if len(self.dct) > self.capacity:
            del self.dct[self.head.next.key]
            self.remove(self.head.next)

        print(self.dct)

        
