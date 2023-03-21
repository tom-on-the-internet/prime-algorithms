from __future__ import annotations


class Node:
    left: Node | None = None
    right: Node | None = None

    def __init__(self, value) -> None:
        self.value = value


def find(node: Node | None, value: int) -> bool:
    if not node:
        return False

    if node.value == value:
        return True

    if node.value < value:
        return find(node.right, value)

    return find(node.left, value)


def insert(node: Node | None, value: int):
    if not node:
        return Node(value)

    if node.value < value:
        new_node: Node | None = insert(node.right, value)
        if new_node:
            node.right = new_node
        return

    new_node: Node | None = insert(node.left, value)
    if new_node:
        node.left = new_node


a = Node(25)

b = Node(12)
c = Node(48)

d = Node(5)
e = Node(20)

f = Node(28)
g = Node(400)

h = Node(3)
i = Node(10)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

d.left = h
d.right = i

res = find(a, 5)
print(res)

insert(a, 19)
node = e
for node in [a, b, c, d, e, f, g, h, i]:
    print(f"My value is {node.value}")
    if node.left:
        print(f"My left child is {node.left.value}")
    if node.right:
        print(f"My right child is {node.right.value}")
