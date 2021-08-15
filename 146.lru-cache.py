#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, val) -> None:
        self.next = None
        self.previous = None
        self.key = key
        self.val = val

    def add(self, node):
        node.previous = self
        node.next = self.next
        self.next.previous = node
        self.next = node
        
    def remove(self):
        if self.previous != None:
            self.previous.next = self.next
        if self.next != None:
            self.next.previous = self.previous

class LRUCache:

    def __init__(self, capacity: int):
        self.dct = {}
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def moveToHead(self, node):
        node.remove()
        self.head.add(node)

    def get(self, key: int) -> int:
        if not key in self.dct:
            return -1
        else:
            node = self.dct[key]
            self.moveToHead(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if not key in self.dct:
            node = Node(key, value)
            self.dct[key] = node
            self.moveToHead(node)

            if len(self.dct) > self.capacity:
                popped = self.tail.previous
                popped.remove()
                del self.dct[popped.key]
        else:
            node = self.dct[key]
            self.moveToHead(node)
            node.val = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

