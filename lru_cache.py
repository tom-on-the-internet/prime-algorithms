from __future__ import annotations


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.length = 0
        self.lookup = {}

    def set(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.delete(self.lookup[key])

        node = Node(key, value)

        self.add(node)

        if self.length > self.capacity:
            self.delete(self.tail)

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]

        self.delete(node)
        self.add(node)

        return node.value

    def remove(self, key: int) -> None:
        if key not in self.lookup:
            return

        self.delete(self.lookup[key])

    def add(self, node: Node) -> None:
        self.length += 1
        self.lookup[node.key] = node
        if not self.head:
            self.head = node
            self.tail = node
            return

        curr_head = self.head
        curr_head.next = node
        node.prev = curr_head
        self.head = node

    def delete(self, node: Node) -> None:
        self.length -= 1
        del self.lookup[node.key]

        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
            return

        if node is self.head:
            self.head = self.head.prev
            self.head.next = None
            return

        if node is self.tail:
            self.tail = self.tail.next
            self.tail.prev = None
            return

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


lru = LRUCache(3)

lru.set(8, 8)
lru.remove(8)
lru.set(7, 7)
lru.set(3, 3)
lru.get(7)
lru.set(7, 7)
lru.set(4, 4)
lru.set(3, 3)
lru.set(2, 2)
lru.set(5, 5)
lru.remove(3)
lru.set(6, 6)

print(lru.length)
print("-")

if lru.head:
    my_head = lru.head
    print(my_head.value)
    while my_head.prev:
        my_head = my_head.prev
        print(my_head.value)
print("-")
print(lru.head.key)
print(lru.tail.key)
