from __future__ import annotations


class Node:
    children: list[Node] = []

    def __init__(self, value) -> None:
        self.value = value


def dfs(node: Node, items: list[int]):
    if not Node:
        return

    items.append(node.value)

    for children in node.children:
        dfs(children, items)


def compare(node1: Node, node2: Node) -> bool:
    if not node1 and not node2:
        return True

    if not node1 or not node2:
        return False

    if node1.value != node2.value:
        return False

    if len(node1.children) != len(node2.children):
        return False

    for idx in range(len(node1.children)):
        if not compare(node1.children[idx], node2.children[idx]):
            return False

    return True


def bfs(root) -> list[int]:
    queue: list[Node] = [root]
    res: list[int] = []

    while queue:
        node = queue.pop(0)
        res.append(node.value)
        queue = queue + node.children

    return res


def find(node: Node, value: int) -> bool:
    if not node:
        return False

    if node.value == value:
        return True

    for child in node.children:
        if find(child, value):
            return True

    return False


a = Node(4)
b = Node(8)
c = Node(3)
d = Node(5)
e = Node(9)
f = Node(1)
g = Node(2)
h = Node(7)
i = Node(6)

a.children = [b, c]
b.children = [d, e, f]
c.children = [g, h]
d.children = [i]

z = Node(4)
b = Node(8)
c = Node(3)
d = Node(5)
e = Node(9)
f = Node(1)
g = Node(2)
h = Node(7)
i = Node(6)

z.children = [b, c]
b.children = [d, e, f]
c.children = [g, h]
d.children = [i]

result = []
dfs(a, result)
print(result)

result = compare(a, z)
print(result)

result = bfs(a)
print(result)

result = find(a, 9)
print(result)
