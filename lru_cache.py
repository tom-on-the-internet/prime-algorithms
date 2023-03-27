from __future__ import annotations

# TODO: Redo this someday.


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

    def add(self, key: int, value: int) -> None:
        node = Node(key, value)
        prev_head = self.head

        self.head = node
        self.head.prev = prev_head

        if prev_head:
            prev_head.next = self.head

        if not self.tail:
            self.tail = node

        # handle if the key already exists
        if key in self.lookup:
            self.remove_node(self.lookup[key])
            self.lookup[key] = node
            return

        self.lookup[key] = node

        if self.length < self.capacity:
            self.length += 1
            return

        self.remove_node(self.tail)

        self.tail = self.tail.next

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]

        if node is self.head:
            return node.value

        prev_head = self.head

        next_node = node.next

        prev_node = node.prev

        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

        self.head = node

        self.head.prev = prev_head

        if prev_head:
            prev_head.next = self.head
            if prev_head.prev is self.head:
                prev_head.prev = None

        return node.value

    def remove_node(self, node):
        if not node:
            return

        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

        del self.lookup[node.key]
        print("removed " + str(node.key))


lru = LRUCache(3)

lru.add(8, 8)  # 8
lru.add(7, 7)  # 7,8
lru.add(3, 3)  # 3,7,8
lru.get(7)  # 7,3,8
lru.add(7, 7)  # 7,3,8
lru.add(4, 4)  # 4,7,3
lru.add(3, 3)  # 3,4,7
lru.add(2, 2)
lru.add(5, 5)
lru.add(6, 6)

print(lru.length)
print("-")

if lru.head:
    my_head = lru.head
    print(my_head.value)
    while my_head.prev:
        my_head = my_head.prev
        print(my_head.value)
print("-")
print(lru.tail.key)
